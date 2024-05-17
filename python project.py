
import pandas as pd
import matplotlib.pyplot as plt
while True:
    print("MAIN MENU")
    print("1.Dataframe Stats")
    print("2.Record Analysis")
    print("3.Insert Delete Record")
    print("4.Data Visualization as per records")
    print("5.Customized Data Visualization")
    print("6.Exit")
    ch=int(input("Enter Your Choice:"))
    if(ch==1):
        df=pd.read_csv("t20wc.csv")
        print("Dataframe Properties:")
        print("1.Diplay the transpose")
        print("2.Display column names")
        print("3.Display indexes")
        print("4.Display the shape")
        print("5.Display the dimension")
        print("6.Display the data types of all columns")
        print("7.Display the size")
        print("8.Back")
        ch1=int(input("Enter Your Choice:"))
        if ch1==1:
            print(df.T)
            input("Press Enter to continue...")
        elif ch1==2:
            print(df.columns)
            input("Press Enter to continue...")
        elif ch1==3:
            print(df.index)
            input("Press Enter to continue...")
        elif ch1==4:
            print(df.shape)
            input("Press Enter to continue...")
        elif ch1==5:
            print(df.ndim)
            input("Press Enter to continue...")
        elif ch1==6:
            print(df.dtypes)
            input("Press Enter to continue...")
        elif ch1==7:
            print(df.size)
            input("Press Enter to continue...")
        elif ch1==8:
            pass
    elif ch==2:
            df=pd.read_csv("t20wc.csv")
            print("RECORD ANALYSIS MENU")
            print("1.Highest Score (Inning - Top 10)")
            print("2.Lowest Score (Inning - Botton 10)")
            print("3.Specific Number of Records From Top")
            print("4.Specific Number of Records From Bottom")
            print("5.Details record for Sr.No.")
            print("6.Details record for a Team")
            print("7.Details record for a Batsman")
            print("8.Most Runs (Top Ten)")
            print("9.Least Runs (Bottom Ten)")
            print("0.Back")
            ch2=int(input("Enter Your Choice:"))
            if ch2==1:
                df1=df.loc[:,['city','name','runs','ballsFaced']]
                df1=df1.sort_values(by='runs',ascending=False)
                print(df1.head(10))
                input("Press Enter to continue...")
            elif ch2==2:
                df1=df.loc[:,['city','name','runs','ballsFaced']]
                df1=df1.sort_values(by='runs',ascending=False)
                print(df1.tail(10))
                input("Press Enter to continue...")
            elif ch2==3:
                no=int(input("How Many Number of Records You Want To Be Printed From The Top:"))
                df1=df.loc[:,['city','name','runs','ballsFaced']]
                print(df1.head(no))
                input("Press enter to continue...")
            elif ch2==4:
                n=int(input("How Many Number of Records You Want To Be Printed From Bottom:"))
                df1=df.loc[:,['city','name','runs','ballsFaced']]
                print(df1.tail(n))
                input("Press enter to continue...")
            elif ch2==5:
                sno=int(input("Enter The Sr.No. For Which You Want The data To Be Displayed:"))
                print(df.loc[sno])
                input('Press enter to continue...')
            elif ch2==6:
                team=input("Enter The Sr.No. For Which You Want The data To Be Displayed:")
                df1=df.loc[df['team']==team]
                print(df1.loc[:,['city','name','runs','ballsFaced']])
                input('Press enter to continue...')
            elif ch2==7:
              print("Ensure the name should match with CSV records:")
              b=input("Enter The Sr.No. For Which You Want The data To Be Displayed:")
              df1=df.loc[df['name']==b]
              print(df1.loc[:,['city','name','runs','ballsFaced']])
              print('------------------------------------------------')
              df1.at['Total','runs']=df1['runs'].sum()
              print(df1)
              input('Press enter to continue...')
            elif ch2==8:
                df1=df[['name','runs']].groupby('name').sum()
                df1=df1.sort_values(by='runs',ascending=False)
                print(df1.head(10))
                input("Press enter to continue...")
            elif ch2==9:
                df1=df[['name','runs']].groupby('name').sum()
                df1=df1.sort_values('runs')
                print(df1.head(10))
                input("Press enter to continue...")
            elif ch2==0:
                pass
            else:
              print("Invalid Choice")
    elif(ch==3):
        df=pd.read_csv("t20wc.csv")
        print("Insert Delete record")
        print("1.Insert a record")
        print("2.Delete a records")
        print("3.Exit The Records Menu")
        ch3=int(input("Enter Your Choice:"))
        if ch3==1:
            col=df.columns
            print(col)
            j=0
            rec={}
            for i in col:
                print("Enter",col[j],"value:")
                nval=input()
                rec[col[j]]=nval
                j=j+1
            df=df.append(rec,ignore_index=True)
            print("Data is Successfully Updated")
            df.to_csv('t20wc.csv',index=False)
            input("Press enter to continue...")
        elif ch3==2:
            a=int(input("Enter S.No. whose data You Want to be deleted:"))
            df.drop([a-1],inplace=True)
            df.to_csv('t20wc.csv',index=False)
            print("Record deleted...")
            input("Press enter to continue...")
        elif ch3==3:
            pass
    elif(ch==4):
        df=pd.read_csv("t20wc.csv")
        print("Data Visualization Menu - According to no. of rows")
        print("1.Line Plot")
        print("2.Vertical Bar Plot")
        print("3.Horizontal Bar Plot")
        print("4.Histogram")
        print("5.Exit The Data Visualization Menu")
        ch4=int(input("Enter Choice:"))
        df1=pd.DataFrame()
        if ch4==1:
            n=int(input("How many records from the top of table you want to plot:"))
            df1=df.head(n)
            df1.plot(linestyle="-.",linewidth=2,label="WORLD CUP RECORD OF MS DHONI")
            plt.show()
        elif ch4==2:
            n=int(input("How many records from the top of table you want to plot:"))
            df1=df.head(n)
            df1.plot(kind="bar",color="pink",width=.8)
            plt.show()
        elif ch4==3:
            n=int(input("How many records from the top of table you want to plot:"))
            df1=df.head(n)
            df1.plot(kind="barh",color="cyan",width=.8)
            plt.show()
        elif ch4==4:
            df.hist(color="yellow",edgecolor="pink")
            plt.show()
        elif ch4==5:
            pass
    elif(ch==5):
        df=pd.read_csv("t20wc.csv")
        print("Customized Data Visualization Menu")
        print("1.By Player")
        print("2.By Team")
        print("3.Back")
        ch5=int(input("Enter Choice:"))
        df1=pd.DataFrame()
        if ch5==1:
            print("Ensure the name should match with CSV records:")
            player=input("Enter player name you want to plot:")
            print('''
                  1. Line Chart
                  2. Bar Chart
                  3. Horizontal Bar Chart
                  4. Histogram
                  5. Back
                  ''')
            ch5_1=int(input("Enter your choice:"))
            if ch5_1==1:
              df1=df.loc[df['name']==player]
              df1=df1.loc[:,['against','runs']]
              df1.plot(x='against',y='runs',kind='line',linestyle="-.",linewidth=2,color='r')
              plt.show()
            elif ch5_1==2:
              df1=df.loc[df['name']==player]
              df1=df1.loc[:,['against','runs']]
              df1.plot(x='against',y='runs',kind='bar',color='r')
              plt.show()
            elif ch5_1==3:
              df1=df.loc[df['name']==player]
              df1=df1.loc[:,['against','runs']]
              df1.plot(x='against',y='runs',kind='barh',color='r')
              plt.show()
            elif ch5_1==4:
              df1=df.loc[df['name']==player]
              df1=df1.loc[:,['against','runs']]
              df1.plot(x='against',y='runs',kind='hist',bins=25,cumulative=True)
              plt.show()
            elif cf5_1==5:
              pass
        elif ch5==2:
            print("Ensure the name should match with CSV records:")
            team=input("Enter team name you want to plot:")
            print('''
                  1. Line Chart
                  2. Bar Chart
                  3. Horizontal Bar Chart
                  4. Histogram
                  5. Back
                  ''')
            ch5_2=int(input("Enter your choice:"))
            if ch5_2==1:
              df1=df.loc[df['team']==team]
              df1=df1.loc[:,['name','runs']]
              df1.plot(x='name',y='runs',kind='line',linestyle="-.",linewidth=2,color='r')
              plt.show()
            elif ch5_2==2:
              df1=df.loc[df['team']==team]
              df1=df1.loc[:,['name','runs']]
              df1.plot(x='name',y='runs',kind='bar',color='r')
              plt.show()
            elif ch5_2==3:
              df1=df.loc[df['team']==team]
              df1=df1.loc[:,['name','runs']]
              df1.plot(x='name',y='runs',kind='barh',color='r')
              plt.show()
            elif ch5_2==4:
              df1=df.loc[df['team']==team]
              df1=df1.loc[:,['name','runs']]
              df1.plot(x='name',y='runs',kind='hist',bins=25,cumulative=True)
              plt.show()
            elif ch5_2==5:
              pass
    elif ch==6:
        print('                          Downloaded from www.tutorialaicsip.com')
        print("Thanks for visiting our blog, for more projects stay tuned with us!!!")
        break
    else:
        print("*---------------------*INVALID CHOICE*---------------------*")
        print('                          Downloaded from www.tutorialaicsip.com           ')
        print("Thanks for visiting our blog, for more projects stay tuned with us!!!")

