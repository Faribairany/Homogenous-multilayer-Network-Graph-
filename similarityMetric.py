#   
from math import radians, cos, sin, asin, sqrt
from numpy import dot
from numpy.linalg import norm 
import string
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer
from nltk.corpus import stopwords
stopwords=stopwords.words('english')
class SimilarityObject:
    def __init__(self):
        print('similarity class initialized')

    # This is for any numeric similarity comparision. Pass the values which need to be compared in obj1 and obj2
    # and the threshold for which the difference can be estimated.


    #in numeric configuration NUMERIC,<i>,<measurement unit of feature i>,METRIC_THRESHOLD,EUCLIDEAN,<threshold value>, 
    # for calculating the euclidean distance since there is only 2 values the following function will work rather than calling the euclidean function as it takes two lists as input
    def numeric_metric(self, obj1, obj2, threshold):  
        try:
               obj1=float(obj1)
               obj2=float(obj2)
        except:
                print('Invalid data!Euclidean distance can be calculated only for float/int values')      
        
        if (abs(obj1 - obj2)) < threshold:
            return True
        else:
            return False

    #calculating the euclidean distance between two different time period (suppose 22:10 and 10:25)
    def numeric_metric_time_range(self, obj1, obj2, list): 
        obj1=obj1.split(':') 
        obj2=obj2.split(':')
        try:
               obj1_hour_portion=float(obj1[0])
               obj2_hour_portion=float(obj2[0])
               obj1_minute_portion=float(obj1[1])
               obj2_minute_portion=float(obj2[1])
        except:
                print('Invalid data! Euclidean distance can be calculated only for float/int values')      
        
        obj1= obj1_hour_portion + float(obj1_minute_portion/60)
        obj2=obj2_hour_portion+float(obj2_minute_portion/60)
        isSimilar=False
        for element in list:
            if (element[0] <= obj1 <= element[1]):
                if (element[0] <= obj2 <= element[1]):
                    isSimilar = True
                    break
                else:
                    isSimilar = False
        return isSimilar


      
      #for calculating the euclidean distance for time attribute
    def numeric_metric_time(self, obj1, obj2, threshold): 
            obj1=obj1.split(':') 
            obj2=obj2.split(':')
            try:
                obj1_hour_portion=float(obj1[0])
                obj2_hour_portion=float(obj2[0])
                obj1_minute_portion=float(obj1[1])
                obj2_minute_portion=float(obj2[1])
            except:
                    print('Invalid data! Euclidean distance can be calculated only for float/int values')      
            
            obj1= obj1_hour_portion + float(obj1_minute_portion/60)
            obj2=obj2_hour_portion+float(obj2_minute_portion/60)
            if (abs(obj1 - obj2)) < threshold:
                return True
            else:
                return False


    #calculating the euclidean distance between two different date DAY/MONTH/YEAR
    def numeric_metric_date(self, period, obj1, obj2, threshold): 

        if period=='WEEK':
            obj1=int(obj1)
            obj2=int(obj2)
            if (abs(obj1 - obj2)) < threshold:
                return True
            else:
                return False
       
        #try different formats for date
        if "/" in obj1 : 
            obj1=obj1.split('/') 
            # print ("Yes, String found") 
        else : 
            if "-" in obj1: 
                obj1=obj1.split('-') 
            else:
                print("Trying another format!")
            # print ("No, String not found") 


        if "/" in obj2: 
            obj2=obj2.split('/') 
            # print ("Yes, String found") 
        else : 
            if "-" in obj2: 
                obj2=obj2.split('-')
            else:
                print("Invalid format")
            # print ("No, String not found")     

        if period=="DAY":
            obj1=obj1[0] 
            obj2=obj2[0]
        elif period=="MONTH":
            obj1=obj1[1]  
            obj2=obj2[1]
        elif period=="YEAR":
            obj1=obj1[2] 
            obj2=obj2[2]
            
        obj1=int(obj1)
        obj2=int(obj2)
        if (abs(obj1 - obj2)) < threshold:
            return True
        else:
            return False

#calculating the metric equality between two different date DAY/MONTH/YEAR
    def numeric_metric_date_equality(self, period, obj1, obj2): 
        # print(type(obj1))
        # print(type(obj2))
        #try different formats for date
        if "/" in obj1 : 
            obj1=obj1.split('/') 
            # print ("Yes, String found") 
        else : 
            if "-" in obj1: 
                obj1=obj1.split('-') 
            else:
                return False
            # print ("No, String not found") 


        if "/" in obj2: 
            obj2=obj2.split('/') 
            # print ("Yes, String found") 
        else : 
            if "-" in obj2: 
                obj2=obj2.split('-') 

            else:
                return False
            # print ("No, String not found") 
        
        if period=="DAY":
            obj1=obj1[0] 
            obj2=obj2[0]
        elif period=="MONTH":
            obj1=obj1[1]  
            obj2=obj2[1]
        elif period=="YEAR":
            obj1=obj1[2] 
            obj2=obj2[2]
            
        if obj1==obj2:
            return True
        else:
            return False

    
    def numeric_metric_self(self,obj,threshold):
        if obj<threshold:
            return True
        else:
            return False

    def nominal_metric(self, object1, object2):
        if object1==object2:
            return True
        else:
            return False


     #for calculating the euclidean distance for time attribute for metric type threshold_segment
    def numeric_metric_time_threshold_segment(self, obj1, obj2, number_of_equi_sized_segment,threshold): 
            
            obj1=obj1.split(':') 
            obj2=obj2.split(':')
            try:
                obj1_hour_portion=float(obj1[0])
                obj2_hour_portion=float(obj2[0])
                obj1_minute_portion=float(obj1[1])
                obj2_minute_portion=float(obj2[1])
            except:
                    print('Invalid data! Euclidean distance can be calculated only for float/int values')                  
            obj1= obj1_hour_portion + float(obj1_minute_portion/60)
            obj2=obj2_hour_portion+float(obj2_minute_portion/60)
            
            segment_value=24/int(number_of_equi_sized_segment)
    
            #if statement checks whether the segment value is int or not
            if int(segment_value)-segment_value==0:
                obj1_start=0
                obj1_end=segment_value
                obj2_start=0
                obj2_end=segment_value
                i=0
                j=0
                while(obj1_end<=24):
                    i=i+1                    
                    if obj1_start<=obj1<=obj1_end:
                        break
                    obj1_start=obj1_start+segment_value
                    obj1_end=obj1_end+segment_value
                while(obj2_end<=24):
                    j=j+1                    
                    if obj2_start<=obj2<=obj2_end:
                        break
                    obj2_start=obj2_start+segment_value
                    obj2_end=obj2_end+segment_value
                if (abs(i - j)) < threshold:
                    return True
                else:
                    return False            
            else:
                print("The segment should be equi-sized!")
                return False
                            
    def haversine(self, lon1, lat1, lon2, lat2,user_unit,threshold):
        distance = 0
        lon1=float(lon1)
        lon2=float(lon2)
        lat1=float(lat1)
        lat2=float(lat2)

        from haversine import haversine, Unit
        # Calculate distance based on the provided units from user
        if user_unit==Unit.KILOMETERS.name:
            distance = haversine((lon1,lat1),(lon2,lat2),unit=Unit.KILOMETERS)
        elif user_unit==Unit.METERS.name:
            distance = haversine((lon1,lat1),(lon2,lat2),unit=Unit.METERS)
        elif user_unit==Unit.MILES.name:
            distance = haversine((float(lon1),float(lat1)),(float(lon2),float(lat2)),unit=Unit.MILES)
        elif user_unit == Unit.NAUTICAL_MILES.name:
            distance = haversine((lon1,lat1),(lon2,lat2),unit=Unit.NAUTICAL_MILES)
        else:
            return False
    
        # verify if the distance is in threshold or not
        if(distance<threshold):
            return True
        else:
            return False
        
    
    def euclidean(self,list1,list2,threshold ):
            # this method has limitation. It should atlease have a 2 dimentional array or more but not less(1 or 0)
            import math
            # this calculates for n- dimentional arrays .... can give directly array with 2 or 3 dimentional elements
            import numpy as np
            #check if th elements of list 1 and 2 can be converted into float values or not  
            try:
                list1=list(np.float_(list1))
                list2=list(np.float_(list2))
            except:
                print('Invalid data!Euclidean distance can be calculated only for float/int values')
                
            distance = math.sqrt(sum([(a - b) ** 2 for a, b in zip(list1, list2)]))

            if(distance<threshold):
                return True
            else:
                return False

    def numeric_metric_range(self,input1,input2,list):
        # Code for checking if the provided input1 and input2 are in any range available in the list(have multiple ranges)
        # If both input1 and input2 are in same range, then we have a edge and return true from this method else false
        isSimilar=False
        for element in list:

            if float(element[0]) <= float(input1) <= float(element[1]):
                if float(element[0]) <= float(input2) <= float(element[1]):
                    isSimilar = True
                    break            
                else:
                        isSimilar = False
            else:
                    isSimilar = False

        return isSimilar
  
#numeric metric range location
        # def numeric_metric_range(self,input1,input2,list):
        # # Code for checking if the provided input1 and input2 are in any range available in the list(have multiple ranges)
        # # If both input1 and input2 are in same range, then we have a edge and return true from this method else false
        # # isSimilar=False
        #     for element in list:

        #         if float(element[0]) <= float(input1) <= float(element[1]):
        #             if float(element[0]) <= float(input2) <= float(element[1]):
        #                 isSimilar = True
        #                 break
        #             else:
        #                 isSimilar = False
                    
        #         else:
        #             isSimilar = False
        #     return isSimilar

#calculation of the cosine similarity between two numeric list of equal size
    def cosine_similarity_numeric_value(self,vec1,vec2,threshold):  
        vec1=vec1.split(',')
        vec2=vec2.split(',')  
        list1=[]
        list2=[]
        for item in vec1:
            list1.append(float(item))
        for item in vec2:
            list2.append(float(item))
        if len(list1)==len(list2):                 
            cos_sim = dot(list1,list2)/(norm(list1)*norm(list2))
            if (cos_sim>=threshold):
                return True
            else:
                return False
        else:
            print("cosine similarity cannot be calculated for list of different size!")
    
    

#for calculating the cosine similarity of two vectors where both the vectors are string
    def cosine_similarity_string_value(self,vec1,vec2,threshold):
        def clean_string(text):        
            text=''.join([word for word in text if word not in string.punctuation])
            text=text.lower()
            text=' '.join([word for word in text.split() if word not in stopwords])
            return text
        
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
        
        
    
    # list accepts integer, float and string types and similarity ranges from 0.0 - 1.0
    def jaccard_similarity(self,list_1,list_2,threshold):
        # remove , from the array and convert it into a list
        list1=set(list_1.split(','))
        list2=set(list_2.split(','))
        common = list1.intersection(list2)
        similarity=float(len(common)) / (len(list1) + len(list2) - len(common))
        if (similarity>=threshold):
            return True
        else:
            return False

        # calculating the similarity of two text and similarity ranges from 0.0 - 1.0
    def jaccard_similarity_text(self,list_1,list_2,threshold):
        # remove , from the array and convert it into a list
        list1=list_1.split()
        list2=list_2.split()
        list1=set(list1)
        list2=set(list2)
        common = list1.intersection(list2)
        similarity=float(len(common)) / (len(list1) + len(list2) - len(common))
        if (similarity>=threshold):
            return True
        else:
            return False
        # """
        # https://stackoverflow.com/questions/4913349/haversine-formula-in-python-bearing-and-distance-between-two-gps-points
        # Calculate the great circle distance between two points
        # on the earth (specified in decimal degrees)
        # """
        # # convert decimal degrees to radians
        # lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])

        # # haversine formula
        # dlon = lon2 - lon1
        # dlat = lat2 - lat1
        # a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
        # c = 2 * asin(sqrt(a))
        # r = 3956  # Radius of earth in kilometers. Use 3956 for miles and 6371 for kms
        # return c * r

    # def geometric(self,lon1,lat1,lon2,lat2,threshold):
    #     distance = SimilarityObject.haversine(lon1,lat1,lon2,lat2)
    #     return SimilarityObject.numeric_metric_self(distance, threshold)
