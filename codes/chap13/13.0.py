import xml.etree.ElementTree as ET

data = '''
<person>
  <name>Gaurav</name>
  <phone type="intl">
  654987321
  </phone>
  <email hide="yes"/>
</person>'''

tree = ET.fromstring(data)
#print(tree)
print('Name : ', tree.find('name').text)
print('Attribute : ', tree.find('email').get('hide'))
