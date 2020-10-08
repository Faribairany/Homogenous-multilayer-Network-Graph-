import enum

metric_type = {
    'NOMINAL': 'NOMINAL',
    'NUMERIC': 'NUMERIC',
    'LOCATION':'LOCATION',
    'SET':'SET',
    'TEXT':'TEXT',
    'TIME':'TIME',
    'DATE':'DATE',
    # 2: 'LOCATION',
    # 3: 'TIME',
    # 4: 'DATE',
    # 5: 'SET',
    # 6: 'TEXT'
}



class UserInput:
    def __init__(self, metric_type, feature_column, distance_measurement, period_measurement, metric_similarity_measure,
                 threshold_input,feature_column_lat,feature_column_long,distance_formulae,similarity_measure_formulae, number_of_range, range_input, number_of_equi_sized_segment):
        self.threshold_input = threshold_input
        self.metric_similarity_measure = metric_similarity_measure
        self.period_measurement = period_measurement
        self.distance_measurement = distance_measurement
        self.feature_column = feature_column
        self.feature_column_lat = feature_column_lat
        self.feature_column_long = feature_column_long
        self.metric_type = metric_type
        self.distance_formulae = distance_formulae
        self.similarity_measure_formulae = similarity_measure_formulae
        self.number_of_range= number_of_range
        self.range_input=range_input
        self.number_of_equi_sized_segment=number_of_equi_sized_segment
        

# initializing everything to NULL
userInputObj = UserInput(None,None,None,None,None,None,None,None,None,None, None, None, None)
# class UserInput:
#     threshold_input = None
#     metric_similarity_measure = None
#     period_measurement = None
#     distance_measurement = None
#     feature_column = None
#     metric_type = None

class InputType:
    NOMINAL_FeatureColumn_METRIC_EQUALITY = 1
    NUMERIC_FeatureColumn_MILES_KM_METRIC_THRESHOLD_EUCLIDEAN_Threshold_input = 2
    NUMERIC_FeatureColumn_MILES_KM_METRIC_FIXEDRANGE_RANGE_INPUT=7
    LOCATION_LatCol_LongCol_MILES_KM_METRIC_THRESHOLD_HAVERSINE_EUCLIDIAN_Threshold_input=3
    # LOCATION_LatCol_LongCol_MILES_KM_METRIC_THRESHOLD_HAVERSINE_EUCLIDIAN_Threshold_input
    LOCATION_LatCol_LongCol_MILES_KM_METRIC_FIXEDRANGE_NUMBER_Of_RANGE_RANGES=13    
    DATE_FeatureColumn_METRIC_THRESHOLD_EUCLIDEAN_DAY_WEEK_MONTH_YEAR_threshold_value=8
    DATE_FeatureColumn_METRIC_EQUALITY_DAY_WEEK_MONTH_YEAR=9
    TIME_FeatureColumn_METRIC_THRESHOLD_EUCLIDEAN_threshold_value=10
    TIME_FeatureColumn_METRIC_FIXEDRANGE_NUMBER_Of_RANGE_RANGES=11
    TIME_FeatureColumn_METRIC_THRESHOLD_SEGMENT_EUCLIDEAN_NUMBER_OF_SEGMENT_threshold_value=12
    SET_FeatureColumn_METRIC_THRESHOLD_COSINE_JACARD_Threshold_input=4
    TEXT_FeatureColumn_METRIC_THRESHOLD_COSINE_JACARD_Threshold_input=5
    INPUT_TYPE_INVALID = 6
    



distance_measurement = {
    'MILES': 'MILES',
    'KM': 'KM'
}

distance_formulae = {
    'HAVERSINE':'HAVERSINE',
    'EUCLIDEAN':'EUCLIDEAN'
}
period_measurement = {
    'DAY': 'DAY',
    'WEEK': 'WEEK',
    'MONTH': 'MONTH',
    'YEAR': 'YEAR'
}

metric_similarity_measure = {
    'METRIC_EQUALITY': 'METRIC_EQUALITY',
    'METRIC_THRESHOLD': 'METRIC_THRESHOLD',
    'METRIC_FIXEDRANGE': 'METRIC_FIXEDRANGE',
    'METRIC_FIXEDRANGE_SEGMENT': 'METRIC_FIXEDRANGE_SEGMENT',
    'METRIC_THRESHOLD_SEGMENT': 'METRIC_THRESHOLD_SEGMENT'
}

class Metric_Similarity_Measure_enum(enum.Enum):
    METRIC_EQUALITY=1
    METRIC_THRESHOLD=2
    METRIC_FIXEDRANGE=3
    METRIC_FIXEDRANGE_SEGMENT=4
    METRIC_THRESHOLD_SEGMENT=5


class Metric_Distance_Measure_enum(enum.Enum):
    HAVERSINE=1
    EUCLIDEAN=2

class Similarity_Measure_Formulae_enum(enum.Enum):
    COSINE=1
    JACCARD=2
    PEARSON=3

def check_if_int(int_input):
    if isinstance(int_input, int):
        return True
    else:
        return False


def is_float(value):
  try:
    float(value)
    return True
  except:
    return False



def NOMINAL(input_array):
        # print("user has opted for Nominal")
        # NOMINAL, < i >, METRIC_EQUALITY
        print("Entered nominal")
        feature_column_input = input_array[1]
        if check_if_int(int(feature_column_input)):
            userInputObj.feature_column = int(feature_column_input)
            print(userInputObj.feature_column)
            metric_similarity_input = input_array[2]
            if metric_similarity_input == metric_similarity_measure.get('METRIC_EQUALITY'):
                # print('input is valid')
                userInputObj.metric_type = InputType.NOMINAL_FeatureColumn_METRIC_EQUALITY
                return userInputObj
            else:
                userInputObj.metric_type = InputType.INPUT_TYPE_INVALID
                # userInputObj.errorMessage = 'invalid metric similarity measure. should be Mertric_equality or Metric_threshold'
                return userInputObj
        else:
            userInputObj.metric_type = InputType.INPUT_TYPE_INVALID
            return userInputObj

def NUMERIC(input_array):
    # NUMERIC, 10, MILES, METRIC_THRESHOLD, 11
    feature_column_input = input_array[1]
    if check_if_int(int(feature_column_input)):
        userInputObj.feature_column = int(feature_column_input)
        metric_distance_measure_input = input_array[2]
        # check if Distance measurement is KM or MILES
        if distance_measurement.get(metric_distance_measure_input, "NONE") != "NONE":
            userInputObj.distance_measurement=metric_distance_measure_input
            metric_similarity_measure_input = input_array[3]
            # check if  or ..any other metric is specified  .......Need to modify ..currently wrong ..need to compare with METRIC_THRESHOLD
            if metric_similarity_measure_input == Metric_Similarity_Measure_enum.METRIC_THRESHOLD.name:
                if input_array[4]==Metric_Distance_Measure_enum.EUCLIDEAN.name:
                    if check_if_int(int(input_array[5])):
                        userInputObj.threshold_input=int(input_array[5])
                        userInputObj.metric_type = InputType.NUMERIC_FeatureColumn_MILES_KM_METRIC_THRESHOLD_EUCLIDEAN_Threshold_input
                        return userInputObj
                    else:
                        return InputType.INPUT_TYPE_INVALID
                else:
                    return InputType.INPUT_TYPE_INVALID
                
            elif metric_similarity_measure_input == Metric_Similarity_Measure_enum.METRIC_FIXEDRANGE.name:
                # Here comes the range related code for numeric
                number_of_range_inputs = int(input_array[4])

                if check_if_int(int(number_of_range_inputs)):
                    userInputObj.number_of_range = number_of_range_inputs
                    final_list = []
                    for i in range(1, number_of_range_inputs + 1):
                        list = final_range_list(input_array[4 + i])
                        final_list.append(list)
                    userInputObj.metric_type = InputType.NUMERIC_FeatureColumn_MILES_KM_METRIC_FIXEDRANGE_RANGE_INPUT
                    userInputObj.range_input = final_list
                    return userInputObj	
                else:
                    return InputType.INPUT_TYPE_INVALID					   
            else:
                return InputType.INPUT_TYPE_INVALID
        else:
            return InputType.INPUT_TYPE_INVALID
    else:
        return InputType.INPUT_TYPE_INVALID


def SET(input_array):
     # check if provided feature column id is int or not. If not, return error
    if check_if_int(int(input_array[1])):
        userInputObj.feature_column = int(input_array[1])
         # check if similarity metric measure is METRIC_THRESHOLD or ..any other metric is specified
        if input_array[2] == Metric_Similarity_Measure_enum.METRIC_THRESHOLD.name:
            if (input_array[3] == Similarity_Measure_Formulae_enum.JACCARD.name) or(input_array[3]==Similarity_Measure_Formulae_enum.COSINE.name) or (input_array[3]==Similarity_Measure_Formulae_enum.PEARSON.name) :
                userInputObj.similarity_measure_formulae=input_array[3]
                if(is_float(input_array[4])):   #checks if the input is float or not
                    userInputObj.threshold_input=float(input_array[4])
                    userInputObj.metric_type = InputType.SET_FeatureColumn_METRIC_THRESHOLD_COSINE_JACARD_Threshold_input
                else:
                    return InputType.INPUT_TYPE_INVALID
            else:
                return InputType.INPUT_TYPE_INVALID
        else:
            return InputType.INPUT_TYPE_INVALID
    else:
        return InputType.INPUT_TYPE_INVALID
                    
def TEXT(input_array):
     # check if provided feature column id is int or not. If not, return error
    if check_if_int(int(input_array[1])):
        userInputObj.feature_column = int(input_array[1])
         # check if similarity metric measure is METRIC_THRESHOLD or ..any other metric is specified
        if input_array[2] == Metric_Similarity_Measure_enum.METRIC_THRESHOLD.name:
            if ((input_array[3] == Similarity_Measure_Formulae_enum.JACCARD.name) or(input_array[3]==Similarity_Measure_Formulae_enum.COSINE.name)):
                userInputObj.similarity_measure_formulae=input_array[3]
                if(is_float(input_array[4]) or check_if_int(input_array[4])):   #checks if the input is float or not
                    userInputObj.threshold_input=float(input_array[4])
                    userInputObj.metric_type = InputType.TEXT_FeatureColumn_METRIC_THRESHOLD_COSINE_JACARD_Threshold_input
                else:
                    return InputType.INPUT_TYPE_INVALID
            else:
                return InputType.INPUT_TYPE_INVALID
        else:
            return InputType.INPUT_TYPE_INVALID
    else:
        return InputType.INPUT_TYPE_INVALID


def LOCATION(input_array):
    # LOCATION,<latitude feature ID, say i>,<longitudefeature ID, say j>,<MILES/KM>,METRIC_THRESHOLD,<HAVERSINE/EUCLIDEAN>,<thresholdvalue>
    # check if provided feature column id is int or not. If not, return error
    if check_if_int(int(input_array[1])) and check_if_int(int(input_array[2])):
        # Assigning values to the user object which will be sent to main method for file processing 
        userInputObj.feature_column_lat = int(input_array[1])
        userInputObj.feature_column_long = int(input_array[2])
         # check if Distance measurement is KM or MILES
        if distance_measurement.get(input_array[3], "NONE") != "NONE":
            userInputObj.distance_measurement=input_array[3]
            # metric_similarity_measure_input = input_array[4]
             # check if similarity metric measure is METRIC_THRESHOLD or ..any other metric is specified
            #if input_array[4] == Metric_Similarity_Measure_enum.METRIC_THRESHOLD:
            if input_array[4] == Metric_Similarity_Measure_enum.METRIC_THRESHOLD.name:
                
                # check if the distance is calculated using haversine or euclidean
                if distance_formulae.get(input_array[5], "NONE") != "NONE":
                    userInputObj.distance_formulae=input_array[5]
                    if(is_float(input_array[6]) or check_if_int(input_array[6])):   #checks if the input is float or not
                        userInputObj.threshold_input=float(input_array[6])
                        userInputObj.metric_type = InputType.LOCATION_LatCol_LongCol_MILES_KM_METRIC_THRESHOLD_HAVERSINE_EUCLIDIAN_Threshold_input
                    else:
                        return InputType.INPUT_TYPE_INVALID
                else:
                    return InputType.INPUT_TYPE_INVALID
            
            elif input_array[4] == Metric_Similarity_Measure_enum.METRIC_FIXEDRANGE.name:
                number_of_range_inputs = int(input_array[5])
                if check_if_int(int(number_of_range_inputs)):
                    userInputObj.number_of_range = number_of_range_inputs
                    final_list = []
                    for i in range(1, number_of_range_inputs + 1):
                        list = final_range_list(input_array[5 + i])
                        final_list.append(list)
                    userInputObj.metric_type = InputType.LOCATION_LatCol_LongCol_MILES_KM_METRIC_FIXEDRANGE_NUMBER_Of_RANGE_RANGES
                    userInputObj.range_input = final_list
                    return userInputObj	
                    
                else:
                    return InputType.INPUT_TYPE_INVALID
            else:
                return InputType.INPUT_TYPE_INVALID
        else:
            return InputType.INPUT_TYPE_INVALID
    else:
        return InputType.INPUT_TYPE_INVALID


def TIME(input_array):
        #print("user has opted for Nominal")        
        print("Entered time")
        feature_column_input = input_array[1]
        if check_if_int(int(feature_column_input)):
            userInputObj.feature_column = int(feature_column_input)
            print(userInputObj.feature_column)
            metric_similarity_input = input_array[2]
    
            if metric_similarity_input == metric_similarity_measure.get('METRIC_THRESHOLD'):           
                if input_array[3]==Metric_Distance_Measure_enum.EUCLIDEAN.name:
                    if check_if_int(int(input_array[4])):
                        userInputObj.threshold_input=int(input_array[4])                   
                        userInputObj.metric_type = InputType.TIME_FeatureColumn_METRIC_THRESHOLD_EUCLIDEAN_threshold_value 
                        return userInputObj
                    else:
                        return InputType.INPUT_TYPE_INVALID
                else:
                    return InputType.INPUT_TYPE_INVALID

            # TIME_FeatureColumn_METRIC_FIXEDRANGE_NUMBER_Of_RANGE_RANGES
            elif metric_similarity_input == Metric_Similarity_Measure_enum.METRIC_FIXEDRANGE.name:
                number_of_range_inputs = int(input_array[3])

                if check_if_int(int(number_of_range_inputs)):
                    userInputObj.number_of_range = number_of_range_inputs
                    final_list = []
                    for i in range(1, number_of_range_inputs + 1):
                        list = final_range_list(input_array[3 + i])
                        final_list.append(list)
                    userInputObj.metric_type = InputType.TIME_FeatureColumn_METRIC_FIXEDRANGE_NUMBER_Of_RANGE_RANGES
                    userInputObj.range_input = final_list
                    return userInputObj	
                else:
                    return InputType.INPUT_TYPE_INVALID	
            
            #TIME_FeatureColumn_METRIC_THRESHOLD_SEGMENT_EUCLIDEAN_NUMBER_OF_EQUI_SIZED_SEGMENT_threshold_value
            elif metric_similarity_input == metric_similarity_measure.get('METRIC_THRESHOLD_SEGMENT'):
                # metric_distance_formulae= input_array[3]             
                if input_array[3]==Metric_Distance_Measure_enum.EUCLIDEAN.name:
                    userInputObj.distance_formulae=input_array[3]                 
                    if check_if_int(int(input_array[4])):
                        userInputObj.number_of_equi_sized_segment=input_array[4]
                        if check_if_int(int(input_array[5])):
                            userInputObj.threshold_input=int(input_array[5])                   
                            userInputObj.metric_type = InputType.TIME_FeatureColumn_METRIC_THRESHOLD_SEGMENT_EUCLIDEAN_NUMBER_OF_SEGMENT_threshold_value
                            return userInputObj
                        else:
                            return InputType.INPUT_TYPE_INVALID
                    else:
                        return InputType.INPUT_TYPE_INVALID
                else:
                    return InputType.INPUT_TYPE_INVALID
            else:
                userInputObj.metric_type = InputType.INPUT_TYPE_INVALID
                # userInputObj.errorMessage = 'invalid metric similarity measure. should be Mertric_equality or Metric_threshold'
                return userInputObj
        else:
            userInputObj.metric_type = InputType.INPUT_TYPE_INVALID
            return userInputObj




def DATE(input_array):
        # print("user has opted for Nominal")
        
        print("Entered date")
        feature_column_input = input_array[1]
        if check_if_int(int(feature_column_input)):
            userInputObj.feature_column = int(feature_column_input)
            print(userInputObj.feature_column)
            metric_similarity_input = input_array[2]
            # Code for DATE, < i >, METRIC_EQUALITY, DAY/WEEK/MONTH/YEAR
            if metric_similarity_input == metric_similarity_measure.get('METRIC_EQUALITY'):
                # print('input is valid')                
                metric_period_measure_input= input_array[3]             
                if period_measurement.get(metric_period_measure_input, "NONE") != "NONE":
                    userInputObj.period_measurement=metric_period_measure_input
                    userInputObj.metric_type = InputType.DATE_FeatureColumn_METRIC_EQUALITY_DAY_WEEK_MONTH_YEAR 
                    return userInputObj
                else:
                    return InputType.INPUT_TYPE_INVALID
            # Code for DATE, < i >, METRIC_THRESHOLD,EUCLIDEAN,DAY/WEEK/MONTH/YEAR,threshold value
            elif metric_similarity_input == Metric_Similarity_Measure_enum.METRIC_THRESHOLD.name:
                if input_array[3]==Metric_Distance_Measure_enum.EUCLIDEAN.name:
                    metric_period_measure_input= input_array[4]
                    # metric_period_measure_input= input_array[3]             
                    if period_measurement.get(metric_period_measure_input, "NONE") != "NONE":
                        userInputObj.period_measurement=metric_period_measure_input
                        if check_if_int(int(input_array[5])):
                            userInputObj.threshold_input=int(input_array[5])
                            userInputObj.metric_type = InputType.DATE_FeatureColumn_METRIC_THRESHOLD_EUCLIDEAN_DAY_WEEK_MONTH_YEAR_threshold_value
                            return userInputObj
                        else:
                            return InputType.INPUT_TYPE_INVALID
                        
                    else:
                        return InputType.INPUT_TYPE_INVALID
                  
                else:
                    userInputObj.metric_type = InputType.INPUT_TYPE_INVALID
                # userInputObj.errorMessage = 'invalid metric similarity measure. should be Mertric_equality or Metric_threshold'
                    return userInputObj

            else:
                userInputObj.metric_type = InputType.INPUT_TYPE_INVALID
                # userInputObj.errorMessage = 'invalid metric similarity measure. should be Mertric_equality or Metric_threshold'
                return userInputObj
        else:
            userInputObj.metric_type = InputType.INPUT_TYPE_INVALID
            return userInputObj



#this function the type of period measurement for the date input
def date_period(input_val):
        # print("Entered date_period")
        try:
            period_val=input_val.split(',')
        except:
            print('Trying the other date formate')
        
        # print(len(period_val))
        if len(period_val)==4:
            period_val = period_val[3]
        if len(period_val)==6:
            period_val = period_val[4]

        return period_val
        


class InputValidationObj:
    # ACTS LIKE A SWITCH CASE

    def __init__(self):
        print("input validation initialized")

    def NONE(self):
        print("invalid input")

    def layer_specification_validation(self, layer_input):
        input_array = layer_input.split(',')

        metric_type_input = input_array[0]
        # evaluates a string as code argument and executes function as we are adding () to call a function
        # Takes a default value 'NONE' if does not match anything in the enum metric_type
        # Sending the input in format string as well
        abc=metric_type.get(metric_type_input, "NONE") + "({})".format(input_array)
        if(abc!='NONE'):
            exec(abc)
        else:
            userInputObj.metric_type=InputType.INPUT_TYPE_INVALID
        print(userInputObj)
        return userInputObj


#function that takes each range input and convert it into a list of integers
def final_range_list(range_list):

    if range_list.startswith('[') and range_list.endswith(']'):
        range_list = range_list[1:-1]

    # splitting the elements basing on -
    range_list = range_list.split("-")

   # print(range_list)

    # converting the string elements of list to integer
    for i in range(0, len(range_list)):
        range_list[i] = int(range_list[i])

    #print(range_list)

    return range_list