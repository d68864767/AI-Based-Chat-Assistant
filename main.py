
from query_parser import QueryParser

def main():
    parser = QueryParser()
    while True:
        query = input("Enter your query: ")
        response = parser.parse_query(query)
        print("Response: ", response)

if __name__ == "__main__":
    main()

