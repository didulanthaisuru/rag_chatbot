from agent import agent

def main():
    print("Welcome to the AI Financial Assistant!")
    
    while True:
        user_input = input("\nEnter your query (or type 'exit' to quit): ")
        if user_input.lower() == "exit":
            print("Goodbye!")
            break
        response = agent.invoke({"input": user_input})
        print("\nAssistant:", response)

if __name__ == "__main__":
    main()
