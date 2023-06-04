import csv


csv_fl = 'mbb_noempties.csv'
lst = []
zip_d = []
lst_info = []
with open('output.csv', mode='a', newline='') as file3:
    fieldName = ["filename", "width", "height",
                 "class_name", "xmin", "ymin", "xmax", "ymax"]
    writer = csv.writer(file3)
    writer.writerow(fieldName)
    with open(csv_fl, 'r') as csv_file:
        cs_r = csv.reader(csv_file)
        for line in cs_r:
            lst = [line[1].split(' ')[x:x+4]for x in range(0, len(line[1].split(' ')), 4)]
            if len(lst) > 1:
                zip_d = list(zip(*lst))
                x = zip_d 
                lst_info = [line[0], 224, 224, 'coconut_tree', str(" ".join(zip_d[1])),
                            str(" ".join(zip_d[0])), str(" ".join(zip_d[3])), str(" ".join(zip_d[2]))]
                
                writer.writerow(lst_info)
            elif len(lst) == 1:
                lst_info = [line[0], 224, 224, 'coconut_tree', lst[0][1],lst[0][0],lst[0][3],lst[0][2]]
                writer.writerow(lst_info)


                

            
            