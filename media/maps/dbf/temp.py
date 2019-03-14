import dbf

def add_field(table, name, typ, num1, num2=0):
    if typ == N:
        table.addNumeric()
    elif typ == C:
    
    elif typ == M:
    
    
["ID","IDPERC","NUME","TREK1","IMPTOR","LIVVER","LIVH2O","LIVH2O","LIVDIV","NUMC","CALMAX","CORMIN","MINCORDE","DISLIV","AMPBAC","ORIGACQUA","PERQUO1","PERQUO2","HAVV","HCAL","HRIENTRO","MMNAV","KMNAV","OPEIDR","LITOL","CHECKP1","CHECKP2","STAGIONE","VINCOLI","PRES","DESACCV","DESACCM","DESAVV","DESPERC","DESUSC","PROFILO","NOTE"]
    


if (__name__=='__main__'):
    # create a new DBF-File
    table = dbf.Table('TOR_PERC', 'id N(16,0)')
    
    add_field("ID",'N',16,0)
    add_field("IDPERC",'N',16,0)
    add_field("NUME",'C',6,0)
    add_field("TREK1",'C',80)
    add_field("IMPTOR",'C',4,0)
    add_field("LIVVER",'N',1,0)
    add_field("LIVH2O",'N',1,0)
    add_field("LIVH2O",'N',1,0)
    add_field("LIVDIV",'N',1,0)
    add_field("NUMC",'N',1,0)
    add_field("CALMAX",'N',1,0)
    add_field("CORMIN",'N',2,0)
    add_field("MINCORDE",'N',1,0)
    add_field("DISLIV",'N',2,0)
    add_field("AMPBAC",'N',4,0)
    add_field("ORIGACQUA",'N',2,0)
    add_field("PERQUO1",'N',4,0)
    add_field("PERQUO2",'N',4,0)
    add_field("HAVV",'N',5,2)
    add_field("HCAL",'N',5,2)
    add_field("HRIENTRO",'N',5,2)
    add_field("MMNAV",'N',3,0)
    add_field("KMNAV",'N',3,0)
    add_field("OPEIDR",'C',4,0)
    add_field("LITOL",'N',2,0)
    add_field("CHECKP1",'N',5,0)
    add_field("CHECKP2",'N',5,0)
    add_field("STAGIONE",'N',2,0)
    add_field("VINCOLI",'C',250,0)
    add_field("PRES",'M',0,0) 
    add_field("DESACCV",'M',0,0)
    add_field("DESACCM",'M',0,0)
    add_field("DESAVV",'M',0,0)
    add_field("DESPERC",'M',0,0)
    add_field("DESUSC",'M',0,0)
    add_field("PROFILO",'C',255,0)
    add_field("NOTE",'M',0,0)

    dbfn.write("tst.dbf")
    # test new dbf
    print("*** created dbf: ***")
    dbft = Dbf('tst.dbf', readOnly=0)
    print(repr(dbft))

