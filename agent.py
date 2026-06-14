"""
AGENT

Workflow:
1. Connect to MCP server
2. Call read_markdown tool
3. Get markdown content
4. Send content to Gemini
5. Print summary

"""

import asyncio
#for asynchronous programming- allows multiple tasks at a time
import os #environment variables

from dotenv import load_dotenv #loads api key from .env

from mcp import ClientSession #creates a client -connection between agent and mcp_server
from mcp.client.stdio import stdio_client, StdioServerParameters #client communicates to servr using stdin and stdout | StdioServerParameters- tells mcp which server to start

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate #for structured, reusable prompts

load_dotenv() #loads api key to memory

llm=ChatGoogleGenerativeAI(model="gemini-2.5-flash",temperature=0)

async def main():

    server_params=StdioServerParameters(command="python",args=['mcp_server.py'])# equivalent to terminal command python mcp_server.py

    async with stdio_client(server_params) as ( #connects client to server create two communication channels
        read_stream, #receives data
        write_stream #sends data
    ):
        async with ClientSession( #starts actual MCP session so both sides can talk
            read_stream,
            write_stream
        ) as session:
            
            await session.initialize() #performs mcp handshake(ie. communication initialisation)

            print("Connected to MCP Server")            

            while True:
                print("\nSelect action:\n1. Summarize\n2. Word Count\n3. Extract Headings\n4. Exit\n")
                ch=int(input("Enter your choice: "))

                if ch not in [1,2,3]:
                    break
                

                print("\nSelect from available notes: \n1. ai.md \n2. ml.md \n3. neural_networks.d \n4. python.md \n")
                filename=input("Enter note name (exactly as given):")
                print()

                if ch==1:
                    result= await session.call_tool( #calls the tool in mcp_server with args req
                        "read_markdown",
                        {
                            "filepath":f"md_files/{filename}"
                        }
                    )

                    markdown_content=result.content[0].text #read_markdown returns plain string but MCP doesnt return plain strings it wraps it in a structured format. result=CallToolResult( content=[ TextContent(text="Ai isa a....")])


            
                    #print("Markdown received")

                    prompt= ChatPromptTemplate.from_template(
                    """
                        Summarize the following markdown content.

                        Markdown:
                        {content}
                    """
                    )

                    chain = prompt |  llm

                    response=chain.invoke(
                        {
                            "content":markdown_content
                        }
                    )

                    print("\nSUMMARY\n")
                    print(response.content)
                
                elif ch==2:
                    result= await session.call_tool( #calls the tool in mcp_server with args req
                        "count_words",
                        {
                            "filepath":f"md_files/{filename}"
                        }
                    )

                    print("No of words: ",result.content[0].text)

                elif ch==3:
                    headlines = await session.call_tool( #calls the tool in mcp_server with args req
                        "extract_headings",
                        {
                            "filepath":f"md_files/{filename}"
                        }
                    )
                    
                    for i in range(len(headlines.content)):
                        print(headlines.content[i].text) 
                
                


if __name__=="__main__": #only direct run (python agent.py) is allowed, import agent not allowed
    asyncio.run(main())