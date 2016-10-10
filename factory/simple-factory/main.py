from Factory import Factory

def xml(filename):
    factory = Factory(filename)
    xml_factory = factory.getFactory()
    xml_data = xml_factory.parsed_data
    liars = xml_data.findall(".//{}[{}='{}']".format('person',
                                                    'lastName','Liar'))
    for liar in liars:
        print('first name: {}'.format(liar.find('firstName').text))
        print('last name: {}'.format(liar.find('lastName').text))
        [print('phone number ({})'.format(p.attrib['type']),
               p.text) for p in liar.find('phoneNumbers')]
    print()

def json(filename):
    factory = Factory(filename)
    json_factory = factory.getFactory()
    json_data = json_factory.parsed_data
    print('found: {} donuts'.format(len(json_data)))
    for donut in json_data:
        print('name: {}'.format(donut['name']))
        print('price: ${}'.format(donut['ppu']))
        [print('topping: {} {}'.format(t['id'], t['type'])) for t in donut['topping']]

def main():
    xml('../data/person.xml')
    json('../data/donut.json')


if __name__ == '__main__':
    main()
