# A mock tool for a Wikipedia search.
import json

def wikipedia_search(query: str) -> str:
    """Mock wikipedia search that returns facts based on keywords to simulate ReAct tool usage."""
    query_lower = query.lower()
    
    if "titanic" in query_lower:
        return "The movie Titanic was released in 1997."
    elif "1997" in query_lower and "president" in query_lower:
        return "Bill Clinton was the 42nd president of the United States from 1993 to 2001."
    elif "inventor" in query_lower and "world wide web" in query_lower:
        return "Tim Berners-Lee invented the World Wide Web."
    elif "tim berners-lee" in query_lower:
        return "Tim Berners-Lee was born in London, England."
    elif "capital" in query_lower and "england" in query_lower:
        return "The capital of England is London."
    elif "eiffel tower" in query_lower:
        return "The Eiffel Tower is made of wrought iron."
    elif "statue of liberty" in query_lower:
        return "The Statue of Liberty's exterior is made of copper, built on an iron framework."
    elif "inception" in query_lower and "nominated" in query_lower:
        return "Inception was nominated for Best Picture at the 83rd Academy Awards for the year 2010."
    elif "best picture" in query_lower and "2010" in query_lower:
        return "The King's Speech won Best Picture for the 2010 movies."
    elif ("director" in query_lower or "directed" in query_lower) and "king's speech" in query_lower:
        return "The King's Speech was directed by Tom Hooper."
    elif "carbon" in query_lower or "atomic number 6" in query_lower:
        return "Carbon has atomic number 6 and is in Group 14 of the periodic table."
    elif "most of earth's atmosphere" in query_lower:
        return "Nitrogen makes up about 78% of Earth's atmosphere."
    elif "nitrogen" in query_lower:
        return "Nitrogen has atomic number 7 and is in Group 15 of the periodic table."
    elif "j.k. rowling" in query_lower:
        return "J.K. Rowling was born on July 31, 1965."
    elif "george r.r. martin" in query_lower:
        return "George R.R. Martin was born on September 20, 1948."
    elif "highest population" in query_lower and "2023" in query_lower:
        return "As of 2023, India has the highest population in the world."
    elif "time zones" in query_lower and "india" in query_lower:
        return "India has 1 official time zone (IST)."
    elif "ebenezer scrooge" in query_lower:
        return "Ebenezer Scrooge is the protagonist of A Christmas Carol, a novella by Charles Dickens."
    elif "charles dickens" in query_lower:
        return "Charles Dickens was a British writer and social critic."
    elif "capital" in query_lower and "france" in query_lower:
        return "The capital of France is Paris."
    elif "capital" in query_lower and "germany" in query_lower:
        return "The capital of Germany is Berlin."
    elif "paris to berlin" in query_lower or "between france and germany" in query_lower or "waffles" in query_lower:
        return "Belgium is located between France and Germany and is famous for its chocolate and waffles."
    elif "roman god of war" in query_lower:
        return "Mars is the Roman god of war."
    elif "roman goddess of love" in query_lower:
        return "Venus is the Roman goddess of love."
    elif "closer to the sun" in query_lower or "planetary order" in query_lower:
        return "The order of planets closest to the sun: Mercury, Venus, Earth, Mars..."
    
    return "No information found on Wikipedia."
