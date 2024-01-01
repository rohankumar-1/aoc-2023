
#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int main(int argc, char *argv[]){

    // get file
    ifstream f(argv[1]);

    // left and right values
    int l, r;
    string line;

    // hold sum of all lines
    int sum = 0;

    if(f.is_open()){
        // get line into string line
        while(getline(f, line)){
            // find bounds of line
            l = 0;
            r = line.size()-1;

            // find left digit
            int digL = (int) (line[l]-'0');
            while(digL < 0 || digL > 9){
                l++;
                digL = (int) (line[l]-'0');
            }

            int digR = (int) (line[r]-'0');
            while(digR < 0 || digR > 9){
                r--;
                digR = (int) (line[r]-'0');
            }

            string val = "";
            val.push_back(line[l]);
            val.push_back(line[r]);
            sum += stoi(val);
        }
    }

    f.close();

    cout << sum << endl;
}