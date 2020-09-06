import os

os.system("tidy -xml -m  --wrap --indent-with-tabs yes --indent-attributes yes --indent yes --sort-attributes alpha --vertical-space yes --priority-attributes 'android:keyLabel android:keyWidth android:codes android:longCode android:specKey android:isRepeatable android:isSticky android:shortPopupCharacters'  *.xml")