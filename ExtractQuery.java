package Search;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;

import Classes.Path;
import Classes.Query;

public class ExtractQuery {
	BufferedReader br;
	ArrayList<Query> queries = new ArrayList<Query>();
	public ExtractQuery() throws IOException {
		//you should extract the 4 queries from the Path.TopicDir
		//NT: the query content of each topic should be 1) tokenized, 2) to lowercase, 3) remove stop words, 4) stemming
		//NT: you can simply pick up title only for query, or you can also use title + description + narrative for the query content.
		//Title only then
		br = new BufferedReader(new FileReader(Path.TopicDir));
		String line = "";
		String id ="",content = "";
		while((line = br.readLine())!=null){
			if(line.startsWith("<num>")){
				id = line.substring("<num> Number: ".length());
			}else if(line.startsWith("<title>")){
				content = line.substring("<title> ".length());
			}else if(line.contentEquals("</top>")){
				Query query = new Query(id,content);
				queries.add(query);
				
			}
		}
		br.close();
	}
	
	public boolean hasNext()
	{
		return !queries.isEmpty();
	}
	
	public Query next()
	{
		if(queries.isEmpty()){
			return null;
		}else{
			return queries.remove(0);
		}
		
	}
}
