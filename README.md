# testproject
This is a data cleaning practise.
The first file simply keeps one line with the same timestamp and barrio. The key code is: 
    df.drop_duplicates(['timestamp', 'barrio'],inplace = True)

The second file is to delete the redundant lines with the same barrio_id, which has a timestamp within a minute of the last line, sharing the same has_power with the last line.
I think this version is good, but it only has five thousand useful lines. But some letters in the municipio column change to "?". That is an interesting problem and I am trying to fix it.

For the third file, I use SQL to do the work (For the former two methods I use python).  I reduce the duplicates that have the same longitude, latitude, and timestamp. The key code is:
    cursor.execute('select a.OID_,a.latitude,a.longitude from py_test as a ,py_test as b where a.latitude=b.latitude and a.longitude=b.longitude and (a.barrio!=b.barrio or a.municipio!=b.municipio)')

To summarize, the first method is direct and without any hypothesis. The second one supposes that the events being registered in 1 minute with the same longitude and latitude is the same one. The third method requires that only when the reported location and timestamp are exactly the same, then we can consider it as one event.
