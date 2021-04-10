from collections import OrderedDict

favorite_languages ={
    'jen':['python','ruby'],
    'sarah': ['c'],
    'edward':['ruby','go'],
    'phil': ['python','haskell'],
}
od1 = OrderedDict()
od1['jen'] = ['c']
od1['sarah'] = ['python','ruby']
od1['edward'] =['ruby','go']
od1['phil'] = ['python','haskell']

for name,languages in od1.items():
    print(name.title() +" 's favorite languages are: ")

    for language in languages:
        print(language.title())