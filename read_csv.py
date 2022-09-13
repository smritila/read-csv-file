f = open("C:\Python-snippets\Filehandling\products.csv", "r")
file_content = f.read()
file_content_list = file_content.split('\n')

for i in range(1,len(file_content_list)):
    product_info = file_content_list[i].split(',')
    
    product_title = product_info[0]
    product_desc = product_info[1]
    product_amount = int(product_info[2])

    formatted_amount = "${:,}".format(product_amount)
    
    print(f"Product {i}:")
    print(f"Title = {product_title}")
    print(f"Description = {product_desc}")
    print(f"Amount = {formatted_amount}")
    print("-------------------------------")
    

    
    
