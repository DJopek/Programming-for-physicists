def process_dat_file(dat_filename):
    data_dict = {}
    
    with open(dat_filename, 'r') as dat_file:
        header = dat_file.readline().strip().split('\t')
        
        for col in header:
            data_dict[col] = []
        
        for line in dat_file:
            val = line.strip().split('\t')
            
            for col, val in zip(header, val):
                data_dict[col].append(val)
    
    return data_dict

def modify_sinf_file(sinf_filename, output_filename):
    with open(sinf_filename, 'r') as sinf_file:
        lines = sinf_file.readlines()

    with open(output_filename, 'w') as output_file:

        for line in lines:
            if "RowData" in line:
                elements = [element for element in line.split()[1:] if element != "__"]
                output_line = line.replace("__", "____").replace("FF", "FFFF").replace("A", "AAAA")
                # output_file.write(output_line)
                ff_index = int(2)
                ff_y = int(31)
                index_line = lines.index(line) + 1

                for index, element in enumerate(elements):

                    relative_x = str(-(index - ff_index))
                    # print(relative_x)
                    relative_y = str((ff_y - int(index_line)))


                    for i in range(1, len(data_dict['Relative_norm_position_x[mm]'])):
                        # print(data_dict['Relative_norm_position_x[mm]'][i])
                        # print(type(data_dict['Relative_norm_position_x[mm]'][i]))
                        # print(data_dict['Relative_norm_position_y[mm]'][i])
                        # print(data_dict["CCT_dice_mean"][i])

                        if data_dict['Relative_norm_position_x[mm]'][i].strip() == relative_x and data_dict['Relative_norm_position_y[mm]'][i].strip() == relative_y:
                        # if data_dict['Relative_norm_position_x[mm]'][i] == relative_x and data_dict['Relative_norm_position_y[mm]'][i] == relative_y :
                            # print(data_dict["CCT_dice_mean"][i])
                            cct_dice_mean = data_dict['CCT_dice_mean'][i].strip()
                            
                            print(cct_dice_mean)
                            print(element)
                            output_line = line.replace(element, str(round(float(cct_dice_mean))))
                            print("Modified Line:", output_line)
                            output_file.write(output_line)


            # else:
            #     output_file.write(line)




dat_filename = "files_input/output-dices_ALL.dat"
sinf_filename = "files_input/output-dices_SINF.sinf"
output_filename = "files_input/output-dices_CCT.sinf"

data_dict = process_dat_file(dat_filename)
modify_sinf_file(sinf_filename, output_filename)