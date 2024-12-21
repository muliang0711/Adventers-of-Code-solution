def is_valid_order(pages, rules):

    page_index = {page: idx for idx, page in enumerate(pages)}
    for rule in rules:
        x, y = map(int, rule.split('|'))
        if x in page_index and y in page_index:
            if page_index[x] > page_index[y]:
                # print(page_index[x] , page_index[y])
                # sort(pages, rules)
                return False
            
    return True
def sort(pages , rules ) : 
    print(pages , rules )
def find_middle_page(pages):
    return pages[len(pages) // 2]

def process_updates(rules, updates):
    valid_middle_pages = []
    for update in updates:
        pages = list(map(int, update.split(',')))
        if is_valid_order(pages, rules):
            valid_middle_pages.append(find_middle_page(pages))
    return sum(valid_middle_pages)

with open('C:\\code\\PYTHON\\2024Challanges\\DAY5\\data.txt' ,'r') as file :
    data = file.read()
    #'47|53\n97|13\n97|61\n97|47\n75|29\n61|13\n75|53\n29|13\n97|29\n53|29\n61|53\n97|53\n61|29\n47|13\n75|47\n97|75\n47|61\n75|61\n47|29\n75|13\n53|13\n\n75,47,61,53,29\n97,61,53,29,13\n75,29,13\n75,97,47,61,53\n61,13,29\n97,13,75,29,47'

      # Split the data by the blank line
    rules_section, updates_section = data.split('\n\n')
    
    # Split each section into lines
    rules = rules_section.split('\n')
    updates = updates_section.split('\n')

    result = process_updates(rules, updates)
    print(result)

