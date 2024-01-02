#include <fstream>
#include <iostream>
#include <string>
#include <sstream>
#include <unordered_map>

using namespace std;

int main(int argc, char *argv[]){

    // open file
    fstream f(argv[1]);

    // error check
    if(!f.is_open()){
        cout << "file not available" << endl;
        return -1;
    }

    // some variables to fill each iteration
    string line;
    int ans = 0;
    int r, b, g;

    // hold max values in this map
    unordered_map<string, int> mp;

    // iterate through each line
    while(getline(f, line)){
        
        // split line by ':', not needed
        line = line.substr(line.find(':')+1);

        // iterate through each case of semicolon
        stringstream ss(line);
        string val, col;

        // zero out all map values
        mp["red"] = 0;
        mp["green"] = 0;
        mp["blue"] = 0;

        // check if possible by iterating through each val, color pair
        bool POSSIBLE = true;

        // iterate through each value in a game
        while(ss >> val >> col){
            // if necessary, take off last character
            if(col[col.size()-1] == ';' || col[col.size()-1] == ','){
                col = col.substr(0, col.size()-1);
            }

            // update min possible cubes of each color
            mp[col] = max(mp[col], stoi(val));
        }

        // find power of game, and then return
        int temp = 1;
        for(auto p : mp){
            temp *= p.second;
        }

        ans += temp;
    }


    cout << ans << endl;

    return 0;
}