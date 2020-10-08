import csv
from itertools import combinations
from similarityMetric import SimilarityObject
from layer import *
import datetime
from inputValidation import *
import time
#C:\Users\Fariba Afrin Irany\Desktop\ra-multicode\inputfile
path='C:/Users/Fariba Afrin Irany/Desktop/ra-multicode/inputfile'
# path='.\datasets'
import os
for filename in os.listdir(path):
    File_Path=filename
    # ActualPath='C:/Users/Admin/OneDrive/RA/multi layer/Multilayer for Git/datasets/{}'.format(File_Path)

    class Main:
        nodeList = []
        edgeList = []
        similarityObj = SimilarityObject()
        inputValidationObj = InputValidationObj()
        layerObj = LayerObject()
        # inputTypeObj = InputType()
        line_count = 0
        line_dummy_count=1
        userInputObj = UserInput(None,None,None,None,None,None,None,None,None,None,None,None,None)
        
    #Opening config file to fetch the details provided by the user
        with open('config_file_1.txt', mode='r') as config_file:
            number_of_layer=0 #initializing the number of layer that will be created
            lines = config_file.readlines()
            number_of_layers = lines[7]
            for layer in range(int(number_of_layers)):
                n = int(layer) + 8
                # index out of range  and rstrip to remove \n at the end
                feature_row = lines[n].rstrip("\n")
                #Node number currently taken as first column by default ( also can be considered as Unique Id or Primary Key)
                node_column = 0
                # check if the provided input is valid (according to the metric format and sequence) and assign the format which the user has opeted for
                result = inputValidationObj.layer_specification_validation(feature_row)
                # Assigning input from user file to the code flow
                feature_column = result.feature_column
                # if available
                feature_column_latitude=result.feature_column_lat
                feature_column_longitude=result.feature_column_long
                # number_of_ranges=result.number_of_range
                list_of_ranges=result.range_input
                user_distance_measurement=result.distance_measurement
                threshold = result.threshold_input
                user_input_type = result.metric_type
                similarity_measure_input=result.similarity_measure_formulae
                # if available
                distance_formulae=result.distance_formulae
                range_input=result.range_input
                number_of_equi_sized_segment=result.number_of_equi_sized_segment
                #check the encoding of csv file type. The file needs to be opended using that encoding type
                # with open('unt1out.csv') as f:
                #    print(f)
                # with open('metaInfo100Records.csv') as f:
                #    print(f)

                from itertools import combinations
                # with open(File_Path, mode='r',encoding="utf8") as data_file:
                with open(r'C:/Users/Fariba Afrin Irany/Desktop/ra-multicode/inputfile/{}'.format(File_Path), mode='r',encoding="cp1252") as data_file:
                    file_name_array=File_Path.split('.')
                    if(file_name_array[1]=="csv"):
                        csv_reader = csv.reader(data_file, delimiter=',')
                    elif(file_name_array[1]=="tsv"):
                        csv_reader = csv.reader(data_file, delimiter='\t')
                           
                    # csv_reader = csv.reader(data_file, delimiter=',')
                    # a = csv_reader
                    # next(csv_reader) 
                    #  # This is for excluding the header from the data list
                    next(csv_reader, None)
                    combi = combinations(list(csv_reader), 2)
                    
                    # Using If elseif else statement here as artificial switch case is not feasible 
                    #NUMERIC_FeatureColumn_MILES_KM_METRIC_THRESHOLD_EUCLIDEAN_Threshold_input
                    if(user_input_type==2):
                        for i in list(combi):
                            #check if two edges can be connected basing on threshold value
                            if similarityObj.numeric_metric(int(i[0][int(feature_column)]), int(i[1][int(feature_column)]), int(threshold)):
                                edgeList.append(str(i[0][int(node_column)]) + "," + str(i[1][int(node_column)]))
                    
                    #NOMINAL_FeatureColumn_METRIC_EQUALITY
                    elif(user_input_type==1):
                        for i in list(combi):
                            if similarityObj.nominal_metric(i[0][int(feature_column)],i[1][int(feature_column)]):
                                edgeList.append(str(i[0][int(node_column)]) + "," + str(i[1][int(node_column)])) # adds the nodes pass similarity metric has an edge
                    
                    # LOCATION_LatCol_LongCol_MILES_KM_METRIC_THRESHOLD_HAVERSINE_EUCLIDIAN_Threshold_input
                    elif(user_input_type==3):
                        if(distance_formulae==Metric_Distance_Measure_enum.HAVERSINE.name):
                            for i in list(combi):
                                # need to implement lon1, lat1, lon2, lat2,user_unit,threshold
                                if similarityObj.haversine(i[0][feature_column_longitude],i[0][feature_column_latitude],i[1][feature_column_longitude],i[1][feature_column_latitude],user_distance_measurement,threshold):
                                    edgeList.append(str(i[0][int(node_column)]) + "," + str(i[1][int(node_column)]))
                        elif(distance_formulae==Metric_Distance_Measure_enum.EUCLIDEAN.name):
                            for i in list(combi):
                                # need to implement lon1, lat1, lon2, lat2,user_unit,threshold                                
                                if similarityObj.euclidean([i[0][feature_column_longitude],i[0][feature_column_latitude]],[i[1][feature_column_longitude],i[1][feature_column_latitude]],threshold):
                                    edgeList.append(str(i[0][int(node_column)]) + "," + str(i[1][int(node_column)]))
                            # yet to be implemented .....logic for calculating distance and add a edge list
                        # else:
                        #     for i in list(combi):
                        #         if similarityObj.euclidean

                    # LOCATION_LatCol_LongCol_MILES_KM_METRIC_FIXEDRANGE_HAVERSINE_EUCLIDIAN_NUMBER_Of_RANGE_RANGES
                    elif(user_input_type==13):
                        # Code for numeric fixed range
                        for i in list(combi):
                            if similarityObj.numeric_metric_range((i[0][(feature_column_longitude)]), (i[1][( feature_column_latitude)]),range_input ):
                                # if similarityObj.numeric_metric_range((i[0][(feature_column_longitude)]), (i[1][( feature_column_longitude)]),range_input ):
                                    edgeList.append(str(i[0][int(node_column)]) + "," + str(i[1][int(node_column)]))
                    
                    #SET_FeatureColumn_METRIC_THRESHOLD_COSINE_JACARD_Threshold_input
                    elif(user_input_type==4):
                        # code for SET type input
                        if(similarity_measure_input==Similarity_Measure_Formulae_enum.JACCARD.name):
                            for i in list(combi):
                                if similarityObj.jaccard_similarity(i[0][int(feature_column)], i[1][int(feature_column)],threshold ):
                                    edgeList.append(str(i[0][int(node_column)]) + "," + str(i[1][int(node_column)]))

                        elif(similarity_measure_input==Similarity_Measure_Formulae_enum.COSINE.name):
                            # code for cosine in set
                            for i in list(combi):
                                if similarityObj.cosine_similarity_numeric_value((i[0][int(feature_column)]), (i[1][int(feature_column)]),threshold):
                                    edgeList.append(str(i[0][int(node_column)]) + "," + str(i[1][int(node_column)]))
                        else:
                            # code for pearson
                            for i in list(combi):
                                if similarityObj.jaccard_similarity(int(i[0][int(feature_column)]), int(i[1][int(feature_column)]),threshold ):
                                    edgeList.append(str(i[0][int(node_column)]) + "," + str(i[1][int(node_column)]))
                    
                    #TEXT_FeatureColumn_METRIC_THRESHOLD_COSINE_JACARD_Threshold_input
                    elif(user_input_type==5):
                        # code for TEXT type input
                        # for jaccard
                        if(similarity_measure_input==Similarity_Measure_Formulae_enum.JACCARD.name):
                            for i in list(combi):
                                if similarityObj.jaccard_similarity_text((i[0][(feature_column)]), (i[1][(feature_column)]),threshold ):
                                    edgeList.append(str(i[0][int(node_column)]) + "," + str(i[1][int(node_column)]))

                        elif(similarity_measure_input==Similarity_Measure_Formulae_enum.COSINE.name):
                            # code for cosine 
                            for i in list(combi):
                                if similarityObj.cosine_similarity_string_value((i[0][(feature_column)]), (i[1][int(feature_column)]),threshold):
                                    edgeList.append(str(i[0][int(node_column)]) + "," + str(i[1][int(node_column)]))
                        else:
                            # code for pearson
                            for i in list(combi):
                                if similarityObj.jaccard_similarity(int(i[0][int(feature_column)]), int(i[1][int(feature_column)]),threshold ):
                                    edgeList.append(str(i[0][int(node_column)]) + "," + str(i[1][int(node_column)]))
                    
                    #NUMERIC_FeatureColumn_MILES_KM_METRIC_FIXEDRANGE_RANGE_INPUT
                    elif(user_input_type==7):
                        # Code for numeric fixed range
                        for i in list(combi):
                            if similarityObj.numeric_metric_range(int(i[0][int(feature_column)]), int(i[1][int(feature_column)]),list_of_ranges ):
                                edgeList.append(str(i[0][int(node_column)]) + "," + str(i[1][int(node_column)]))

                    # DATE_FeatureColumn_METRIC_THRESHOLD_EUCLIDEAN_DAY_WEEK_MONTH_YEAR_threshold_value=8
                    elif(user_input_type==8):
                        # Code for date metric threshold
                        period=date_period(feature_row)
                        if period=="WEEK":
                            for i in list(combi):
                                if similarityObj.numeric_metric_date(period,i[0][int(feature_column)],i[1][int(feature_column)],threshold):
                                    edgeList.append(str(i[0][int(node_column)]) + "," + str(i[1][int(node_column)]))
                        else:
                            for i in list(combi):
                                if similarityObj.numeric_metric_date(period,i[0][int(feature_column)],i[1][int(feature_column)],threshold):
                                    edgeList.append(str(i[0][int(node_column)]) + "," + str(i[1][int(node_column)]))

                    
                    #DATE_FeatureColumn_METRIC_EQUALITY_DAY_WEEK_MONTH_YEAR=9                     
                    elif(user_input_type==9):
                        # Code for date metric equality
                        period=date_period(feature_row)
                        if period=="WEEK":
                            for i in list(combi):
                                if similarityObj.nominal_metric(i[0][int(feature_column)],i[1][int(feature_column)]):
                                    edgeList.append(str(i[0][int(node_column)]) + "," + str(i[1][int(node_column)])) # adds the nodes pass similarity metric has an edge
                        else:
                            for i in list(combi):
                                if similarityObj.numeric_metric_date_equality(period, i[0][(feature_column)],i[1][(feature_column)]):
                                    edgeList.append(str(i[0][int(node_column)]) + "," + str(i[1][int(node_column)])) # adds the nodes pass similarity metric has an edge
                    
                    #TIME_FeatureColumn_METRIC_THRESHOLD_EUCLIDEAN_threshold_value=10
                    elif(user_input_type==10):
                        # Code for time metric equality                       
                        for i in list(combi):
                            if similarityObj.numeric_metric_time(i[0][int(feature_column)],i[1][int(feature_column)],threshold):
                                edgeList.append(str(i[0][int(node_column)]) + "," + str(i[1][int(node_column)])) # adds the nodes pass similarity metric has an edge
                                
                    #TIME_FeatureColumn_METRIC_FIXEDRANGE_NUMBER_Of_RANGE_RANGES=11
                    elif(user_input_type==11):
                        # Code for time metric fixedrange
                        for i in list(combi):
                            if similarityObj.numeric_metric_time_range(i[0][int(feature_column)],i[1][int(feature_column)],list_of_ranges):
                                edgeList.append(str(i[0][int(node_column)]) + "," + str(i[1][int(node_column)])) # adds the nodes pass similarity metric has an edge

                    #need to work on this portion, not clear how it works
                    # TIME_FeatureColumn_METRIC_THRESHOLD_SEGMENT_EUCLIDEAN_NUMBER_OF_SEGMENT_threshold_value=12
                    elif(user_input_type==12):
                        # Code for date metric equality 
                        for i in list(combi):
                            if similarityObj.numeric_metric_time_threshold_segment(i[0][(feature_column)],i[1][(feature_column)],number_of_equi_sized_segment,threshold):
                                edgeList.append(str(i[0][int(node_column)]) + "," + str(i[1][int(node_column)])) # adds the nodes pass similarity metric has an edge
           
                    else:
                        print("Invalid input provided. Terminating the program. Please check your input format")

                if len(edgeList)==0:
                    print("Layer file cannot be created as no edge is found for the input configuration!")

                if len(edgeList)!=0:
                    with open(r'C:/Users/Fariba Afrin Irany/Desktop/ra-multicode/inputfile/{}'.format(File_Path), mode='r',encoding="utf8") as data_file:
                        # print(data_file)
                        file_name_array=File_Path.split('.')
                        if(file_name_array[1]=="csv"):
                            csv_reader = csv.reader(data_file, delimiter=',')
                            next(csv_reader)
                            for row in csv_reader:
                                nodeList.append(str(row[0]))
                                line_count += 1
                        elif(file_name_array[1]=="tsv"):
                            csv_reader = csv.reader(data_file, delimiter='\t')
                            next(csv_reader)
                            for row in csv_reader:
                                nodeList.append(str(row[0]))
                                line_count += 1

                    # file_name = "layer_file_{}_{}_{}".format(layer+1,feature_column,time.strftime("%Y%m%d-%H%M%S"))
                    # file_name_array=File_Path.split('.')
                    
                    # print(file_name_array[1])
                    #number of layerfile that will be generated(output file name will be layer_file_number_of_layer)
                    number_of_layer=number_of_layer+1
                    file_name="C:/Users/Fariba Afrin Irany/Desktop/ra-multicode/layer_fiiles/layer_file_{}.csv".format(file_name_array[0])
                    if (file_name_array[1]=="csv"):
                         file_name="C:/Users/Fariba Afrin Irany/Desktop/ra-multicode/layer_fiiles/layer_file_{}.txt".format(number_of_layer)
                    elif (file_name_array[1]=="tsv"):
                         file_name="C:/Users/Fariba Afrin Irany/Desktop/ra-multicode/layer_fiiles/layer_file_{}.txt".format(number_of_layer)
                    # calling layer class to write layer data to a file
                    layerObj.write_layer_file(line_count, edgeList, nodeList, file_name)
                    line_count=0
                    nodeList=[]
                    edgeList=[]
            


            
