import re
from info_handler import InfoHandler
from time_date_handler import TimeDateHandler
from calculation_handler import CalculationHandler

class QueryParser:
    def __init__(self):
        self.info_handler = InfoHandler()
        self.time_date_handler = TimeDateHandler()
        self.calculation_handler = CalculationHandler()

    def parse_query(self, query):
        # Check if the query is asking for information
        if re.match(r'^What is', query):
            topic = query[8:]  # Extract the main topic from the query
            return self.info_handler.get_info(topic)

        # Check if the query is asking for the current time or date
        elif re.match(r'^What\'s the time', query) or re.match(r'^What\'s the date', query):
            return self.time_date_handler.get_time_date(query)

        # Check if the query is a calculation
        elif re.match(r'^Calculate', query):
            expression = query[10:]  # Extract the expression from the query
            return self.calculation_handler.calculate(expression)

        else:
            return "Sorry, I didn't understand your query. Please try again."

if __name__ == "__main__":
    parser = QueryParser()
    while True:
        query = input("Enter your query: ")
        response = parser.parse_query(query)
        print("Response: ", response)
