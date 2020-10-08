import string
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer
from nltk.corpus import stopwords
#for calculating the cosine similarity of two vectors where both the vectors are string






def cosine_similarity_string_value(vec1,vec2,threshold):
        def clean_string(text):
        
            text=''.join([word for word in text if word not in string.punctuation])
            text=text.lower()
            text=' '.join([word for word in text.split() if word not in stopwords])
            return text
        threshold=5
        list_vec=[]
        list_vec.append(vec1)
        list_vec.append(vec2)
        cleaned=list(map(clean_string,list_vec))
        vectorizer=CountVectorizer().fit_transform(cleaned)
        vectors=vectorizer.toarray()
        csim=cosine_similarity(vectors)
        vec1=vectors[0].reshape(1,-1)
        vec2=vectors[1].reshape(1,-1)
        similarity_val=cosine_similarity(vec1,vec2)[0][0]
        
        if (similarity_val>=float(threshold)):
            return True
        else:
            return False
stopwords=stopwords.words('english')
val=cosine_similarity_string_value('This is a foo bar sentence.','This sentence is similar to a foo bar sentence.',5)