
#include <fstream>
#include <iostream>
#include <string>

using namespace std;

/* Helper function to check all adjacent characters for being a special character */
bool isValid(vector<string>& grid, int i, int j){
    vector<pair<int, int>> dir = {{-1, -1}, {-1, 0}, {0, -1}, {1, 1}, {1, 0}, {0, 1}, {1, -1}, {-1, 1}};

    for(auto d : dir){
        int di = i + d.first;
        int dj = j + d.second;
        
        if(di < grid.size() && di >= 0 && dj < grid[0].size() && dj >= 0){
            if(grid[di][dj] != '.' && (grid[di][dj] < '0' || grid[di][dj] > '9')){
                return true;
            }
        }
    }

    return false;
}

int main(int argc, char *argv[]){

    int res = 0;

    // open file
    fstream f;
    f.open(argv[1]);

    // fill char array with contents
    vector<string> grid;
    string curr;

    while(getline(f, curr)){
        grid.push_back(curr);
    }

    cout << grid.size() << " " << grid[0].size() << endl;

    // go through each line
    int WIDTH = grid[0].size();
    for(int i = 0; i < grid.size(); i++){

        int j = 0;
        while(j < WIDTH){

            string val = ""; bool valid = false;
            while(j < WIDTH && grid[i][j] >= '0' && grid[i][j] <= '9'){
                // start of a value
                valid |= isValid(grid, i, j);
                val.push_back(grid[i][j]);
                j++;
            }

            if(valid) res += stoi(val);

            j++;
        }
    }

    cout << res << endl;

    return res;
}