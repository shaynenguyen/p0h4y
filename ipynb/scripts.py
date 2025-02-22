import re
import pandas as pd

# Merge list of string into a long text.
def join_txt(list_txt):
    # Join list of content into 1 simple paragraph
    seperator = '. '
    return seperator.join(list_txt)


# Split Url out of content
def get_url(regex, sample):
    result = re.search(regex, sample)

    if result:
#         print(result[0])
        return result[0]

    return ''

# Split text out of content
def split_txt_form_url(sample):
#     print(sample)
#     print("\n")
    
    url = get_url(regex_url,sample)
    if len(url):
        result = sample.replace(url,'')
        result.lstrip().rstrip()
    else:
        result = sample

    return result

# Get hastags out of string.
def get_hastags_out(regex, sample):

    # Find all possible hastags
    result = re.findall(regex,sample)

    return result

# Strip "#" within string
def stript_hastags(sample):
    return sample.replace("#",'')

# Get extend link
def get_extend_link(regex, sample):
    result = []

    # Get the extend link
    for reg in regex:
        # print("Reg: ", reg)
        temp_list = re.findall(reg,sample)
        print("After Regex: ",temp_list)
        print(type(temp_list))
        # result.extend(temp_list)

        # Completely remove from the sample text
        if len(temp_list):
            # print(temp_list)
            # print("\n")
            for ext in temp_list:
                ext = list(ext)
                # print("Ext: ", ext)
                # print("Type: ", type(ext))
                for ex_ in ext: 
                    print("Sub-list: ", type(ex_))
                    if len(ex_) > 3:
                        print("Replace: ", ex_)
                        # sample.replace(ex_,'')
                        result = ex_
        else:
            result = ''

    return result


# Scrapt content base on xpath command.
def scrapt_w_xpath(list_scrapt):
    result = dict()
    print("IN SCRAPT W XPath")

    # # Content
    # contents = xpath_selector.xpath(xpath_cmd[0]).extract()
    # result.update({'contents': contents})
    # print(len(contents))
    
    # # Tags
    # tags = xpath_selector.xpath(xpath_cmd[1]).extract()
    # result.update({'tags': tags})
    # print(xpath_cmd[1] , tags)
    
    # # Author
    # author = xpath_selector.xpath(xpath_cmd[2]).extract()
    # result.update({'author': author})
    # print(xpath_cmd[2],author)

    # Content
    if len(xpath_cmd[0]):
        contents = xpath_selector.xpath(list_scrapt[0]).extract()
        contents = join_txt(contents)
    else:
        contents = ''
    print("Content: ", len(contents))
    
    # Tags
    if len(xpath_cmd[1]):
        tags = xpath_selector.xpath(list_scrapt[1]).extract()
    else:
        tags = ''

    # Author
    if len(xpath_cmd[2]):
        author = xpath_selector.xpath(list_scrapt[2]).extract()
    else:
        author = ''

    # Update object to result
    result.update({
                    'contents': contents,
                    'tags': tags,
                    'author': author
                    })

    print(result)

    
    return result