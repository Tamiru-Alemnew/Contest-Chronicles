#include <iostream>
#include <vector>
#include <set>

using namespace std;

int remaining_walls(int H, int W, int Q, vector<pair<int, int>>& queries) {
    vector<multiset<int>> rowWalls(H + 1), colWalls(W + 1);
    int totalWalls = H * W;

    for (int i = 1; i <= H; ++i) {
        for (int j = 1; j <= W; ++j) {
            rowWalls[i].insert(j);
            colWalls[j].insert(i);
        }
    }

    for (auto& query : queries) {
        int r = query.first;
        int c = query.second;

        if (rowWalls[r].find(c) != rowWalls[r].end()) {
            rowWalls[r].erase(rowWalls[r].find(c));
            colWalls[c].erase(colWalls[c].find(r));
            totalWalls--;
        } else {
            auto itUp = colWalls[c].lower_bound(r);
            if (itUp != colWalls[c].begin()) {
                --itUp;
                int u = *itUp;
                colWalls[c].erase(itUp);
                rowWalls[u].erase(rowWalls[u].find(c));
                totalWalls--;
            }

            auto itDown = colWalls[c].upper_bound(r);
            if (itDown != colWalls[c].end()) {
                int d = *itDown;
                colWalls[c].erase(itDown);
                rowWalls[d].erase(rowWalls[d].find(c));
                totalWalls--;
            }

            auto itLeft = rowWalls[r].lower_bound(c);
            if (itLeft != rowWalls[r].begin()) {
                --itLeft;
                int l = *itLeft;
                rowWalls[r].erase(itLeft);
                colWalls[l].erase(colWalls[l].find(r));
                totalWalls--;
            }

            auto itRight = rowWalls[r].upper_bound(c);
            if (itRight != rowWalls[r].end()) {
                int ri = *itRight;
                rowWalls[r].erase(itRight);
                colWalls[ri].erase(colWalls[ri].find(r));
                totalWalls--;
            }
        }
    }

    return totalWalls;
}

int main() {
    int H, W, Q;
    cin >> H >> W >> Q;
    vector<pair<int, int>> queries(Q);

    for (int i = 0; i < Q; ++i) {
        cin >> queries[i].first >> queries[i].second;
    }

    cout << remaining_walls(H, W, Q, queries) << endl;
    return 0;
}
