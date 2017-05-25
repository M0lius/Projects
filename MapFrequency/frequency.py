import xml.etree.ElementTree as ET
#include <stdio.h>
import sys

def main():
    if len(sys.argv)!= 2:
        print("Incorrent Number Arguments");
        return;

    print("\nGOT MAP: " + sys.argv[1] + "\n");

    tree = ET.parse(sys.argv[1]);
    root = tree.getroot();

    print("\n FINISHED! \n");

if __name__ == "__main__":
    main()
