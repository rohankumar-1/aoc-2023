#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int main(int argc, char *argv[]){
    // digits
    vector<string> digits = {"one", "two", "three", "four", "five", "six", "seven", "eight", "nine"};

    // get file
    ifstream f(argv[1]);

    // left and right idx values
    int l, r;
    string line;

    // strings to check agaisnt digits
    string strLeft, strRight;

    // hold sum of all lines
    int sum = 0;

    if(f.is_open()){

        // get line into string line
        while(getline(f, line)){
            // find bounds of line
            l = 0; r = line.size()-1;

            // current 5 chars held in string
            strLeft.clear(); strRight.clear();

            cout << line << endl;

            // value in this line
            int val = 0;

            // find left digit
            int digL;
            while(1){
                // check for left digit
                digL = (int) line[l]-'0';
                if(digL >= 0 && digL < 10){
                    // we found a number, so we need break out, this is our value
                    val += (digL) * 10;
                    break;
                }

                // update string
                strLeft.push_back(line[l]);
                if(strLeft.size() > 5){
                    strLeft = strLeft.substr(1);
                }

                for(int i = 0; i < digits.size(); i++){
                    string d = digits[i];
                    if(d.size() > strLeft.size()){
                        continue;
                    }
                    if(d == strLeft.substr(strLeft.size()-d.size(), d.size())){
                        val += (i+1)*10;
                        break;
                    }
                }

                if(val > 0) break;

                l++;
            }

            // find right digit
            int digR;
            while(1){
                // check for right digit
                digR = (int) line[r]-'0';
                if(digR >= 0 && digR < 10){
                    // we found a number, so we need break out, this is our value
                    val += digR;
                    break;
                }

                // update string
                strRight = line[r] + strRight;
                if(strRight.size() > 5){
                    strRight = strRight.substr(0, strRight.size()-1);
                }

                // check digits
                for(int i = 0; i < digits.size(); i++){
                    string d = digits[i];
                    if(d.size() > strRight.size()){
                        continue;
                    }
                    if(d == strRight.substr(0, d.size())){
                        val += (i+1);
                        break;
                    }
                }

                if(val % 10 != 0) break;

                r--;
            }

            cout << val << endl;

            sum += val;
        }
    }

    f.close();

    cout << sum << endl;
}