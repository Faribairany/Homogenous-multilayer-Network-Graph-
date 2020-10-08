class LayerObject:
    def __init__(self):
        print('layers initialized')

    def write_layer_file(self, line_count, edge_list, node_list,file_name):
        with open(file_name, mode='w+') as layer_file:
            layer_file.write('Layer 1\n')
            layer_file.write(str(line_count))
            layer_file.write('\n')
            layer_file.write(str(len(edge_list)))
            layer_file.write('\n')
            for i in node_list:
                layer_file.write(str(i) + "\n")
            for i in list(edge_list):
                layer_file.write(str(i))
                layer_file.write(',1.0000 \n')
            
        # import csv
        # with open(file_name, 'w', newline='') as file:
        #     writer = csv.writer(file)
        #     for i in list(edge_list):
        #         before_split=i.split(',')
        #         writer.writerow([before_split[0],before_split[1], 1.000])



        print('layer file writing completed')
