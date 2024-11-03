#import STW
import PTW


crawl = False
prozess = True

def main():
    if crawl:
        print("a")
        #STW.main()
    if prozess:
        PTW.main()
    print("Test")

if __name__ == '__main__':
    main()