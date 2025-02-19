#import STW
import STW2
import PTW


crawl = False
prozess = True

def main():
    if crawl:
        print("a")
        STW2.main()
        #STW.main()
    if prozess:
        PTW.main()
    print("Test")

if __name__ == '__main__':
    main()