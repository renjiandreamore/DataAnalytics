package Search;

import java.io.IOException;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

import Classes.Query;
import Classes.Document;
import IndexingLucene.MyIndexReader;

public class QueryRetrievalModel {
	
	protected MyIndexReader indexReader;
	private int miu = 500;//set to 500 because that is close to the avg posting length.
	private static long collectionFre = 142065539;
	
	public QueryRetrievalModel(MyIndexReader ixreader) {
		indexReader = ixreader;
	}
	
	/**
	 * Search for the topic information. 
	 * The returned results (retrieved documents) should be ranked by the score (from the most relevant to the least).
	 * TopN specifies the maximum number of results to be returned.
	 * 
	 * @param aQuery The query to be searched for.
	 * @param TopN The maximum number of returned document
	 * @return
	 */
	
	public List<Document> retrieveQuery( Query aQuery, int TopN ) throws IOException {
		// NT: you will find our IndexingLucene.Myindexreader provides method: docLength()
		// implement your retrieval model here, and for each input query, return the topN retrieved documents
		// sort the docs based on their relevance score, from high to low
		HashMap<String,Document> docs = new HashMap<String,Document>();
		String[] words = aQuery.GetQueryContent().split(" ");
		int avgLen = 0;
		int count = 0;
		for(String word:words){
			long corFre = indexReader.CollectionFreq(word);
			if(corFre == 0){//skip the word that does not appear
				continue;
			}else{
				int[][] postings = indexReader.getPostingList(word);
				String docNo ="";
				for(int[] posting:postings){
					int docId = posting[0];
					int wordFre = posting[1];
					double score = computeP(wordFre,corFre,indexReader.docLength(docId));
					avgLen += indexReader.docLength(docId);
					count++;
					docNo = indexReader.getDocno(docId);
					if(docs.containsKey(docNo)){
						Document doc = docs.remove(docNo);
						score *= doc.score();
						doc.setScore(score);
					}else{
						Document doc = new Document(""+docId,docNo,score);
						docs.put(docNo, doc);
					}
				}
			}
		}
		List<Document> re = new ArrayList<Document>();
		for (Map.Entry<String, Document> entry : docs.entrySet()) {
	        Document doc  = entry.getValue();
	        if(re.size()<=TopN){
	        	int insertIndex = 0;
	        	for(int i=0;i<re.size();i++){
	        		if(doc.score() > re.get(i).score())	break;
	        		insertIndex++;
	        	}
	        	re.add(insertIndex, doc);
	        }else if(doc.score()>re.get(TopN).score()){
	        	int insertIndex = 0;
	        	for(int i=0;i<re.size();i++){
	        		if(doc.score() > re.get(i).score())	break;
	        		insertIndex++;
	        	}
	        	re.add(insertIndex, doc);
	        	re.remove(TopN);
	        }
	    }
		System.out.println("avg doc words len:"+ avgLen/count);
		return re.subList(0, TopN);
	}
	
	private double computeP(int wordCount,long wordFre,int docLen){
		return (double)(wordCount + miu*((double)wordFre/collectionFre))/(docLen +miu);
	}
	
}