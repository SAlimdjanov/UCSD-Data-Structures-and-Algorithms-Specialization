/**
 * @file tip_removal.cpp
 * @brief Could not get this problem to work in python, so implemented in C++
 * @version 0.1
 * @date 2023-10-12
 *
 * @copyright Copyright (c) 2023
 *
 * TODO: Debug Python solution
 *
 */

#include <iostream>
#include <map>
#include <set>
#include <unordered_map>
#include <vector>

typedef std::vector<int> int_vector;
typedef std::vector<std::vector<int>> vector_of_int_vector;
typedef std::vector<std::set<int>> vector_of_int_set;

class DeBruijnGraph
{
public:
    DeBruijnGraph(int k, int t) : _k(k), _t(t), _v(0) {}

    void addRead(const std::string &read)
    {
        for (int i = 0; i < read.size() - _k + 1; i++)
        {
            std::string kmer = read.substr(i, _k);
            if (_edgeSet.find(kmer) == _edgeSet.end())
            {
                _edgeSet.insert(kmer);
                _edges.push_back(kmer);
            }
        }
    }

    void constructDeBruijnGraph()
    {
        for (auto edge : _edges)
        {
            std::string pre = edge.substr(0, edge.size() - 1);
            std::string suf = edge.substr(1);
            _prefixMap.insert({pre, _v});
            if (_vertexMap.find(pre) == _vertexMap.end())
            {
                _vertices.push_back(pre);
                _vertexMap[pre] = _v++;
            }
            if (_vertexMap.find(suf) == _vertexMap.end())
            {
                _vertices.push_back(suf);
                _vertexMap[suf] = _v++;
            }
        }
        _adjacencyList.resize(_v);
        for (int i = 0; i < _edges.size(); i++)
        {
            std::string pre = _edges[i].substr(0, _edges[i].size() - 1);
            std::string suf = _edges[i].substr(1);
            int to_vertex_index = _vertexMap[suf];
            int from_vertex_index = _vertexMap[pre];
            _adjacencyList[from_vertex_index].push_back(to_vertex_index);
        }
    }

    int totalBubbles()
    {
        int cnt = 0;
        for (int i = 0; i < _adjacencyList.size(); i++)
            if (_adjacencyList[i].size() >= 2)
                cnt += bubblesFromOrigin(i, _t);
        return cnt;
    }

private:
    int _k;
    int _t;
    std::vector<std::string> _edges;
    std::set<std::string> _edgeSet;
    int _v;
    std::vector<std::string> _vertices;
    std::multimap<std::string, int> _prefixMap;
    std::unordered_map<std::string, int> _vertexMap;
    vector_of_int_vector _adjacencyList;

    void nonOverlapPaths(int_vector &path, std::set<int> &visited,
                         vector_of_int_vector &allPaths,
                         vector_of_int_set &allSets, int l)
    {
        if (path.size() == l)
        {
            allPaths.push_back(path);
            allSets.push_back(visited);
            return;
        }

        int s = path.back();

        if (_adjacencyList[s].size() == 0)
        {
            allPaths.push_back(path);
            allSets.push_back(visited);
            return;
        }

        for (int i = 0; i < _adjacencyList[s].size(); i++)
        {
            int v = _adjacencyList[s][i];

            if (visited.find(v) == visited.end())
            {
                visited.insert(v);
                path.push_back(v);
                nonOverlapPaths(path, visited, allPaths, allSets, l);
                path.pop_back();
                visited.erase(v);
            }
            else
            {
                continue;
            }
        }
    }

    std::string PathString(int_vector &leftPath, int_vector &rightPath,
                           int merge)
    {
        std::string ret;
        for (auto &p : leftPath)
            if (p == merge)
            {
                ret += std::to_string(p);
                break;
            }
            else
                ret += std::to_string(p) + ",";

        ret += ";";

        for (auto &p : rightPath)
            if (p == merge)
            {
                ret += std::to_string(p);
                break;
            }
            else
                ret += std::to_string(p) + ",";

        return ret;
    }

    int bubblesFromLeftToRight(vector_of_int_set &leftSet,
                               vector_of_int_set &rightSet,
                               vector_of_int_vector &leftPaths,
                               vector_of_int_vector &rightPaths)
    {
        bool merged;
        std::set<std::string> mergePaths;
        for (int i = 0; i < leftSet.size(); i++)
        {
            auto &s = leftSet[i];
            for (auto &p : rightPaths)
            {
                merged = false;
                for (auto &v : p)
                {
                    if (s.find(v) != s.end())
                    {
                        merged = true;
                        std::string pathString = PathString(leftPaths[i], p, v);
                        mergePaths.insert(pathString);
                        break; // end current path
                    }
                }
                if (merged)
                    continue;
            }
        }
        return mergePaths.size();
    }

    int bubblesFromOrigin(int s, int t)
    {
        int count = 0;
        int_vector path;
        vector_of_int_vector leftPaths, rightPaths;
        vector_of_int_set leftSet, rightSet;
        std::set<int> visited;
        int nPath = _adjacencyList[s].size();
        for (int i = 0; i < (nPath - 1); i++)
        {
            for (int j = i + 1; j < nPath; j++)
            {
                path.clear();
                leftPaths.clear();
                visited.clear();
                leftSet.clear();
                path.push_back(_adjacencyList[s][i]);
                visited.insert(_adjacencyList[s][i]);
                nonOverlapPaths(path, visited, leftPaths, leftSet, t);
                path.clear();
                rightPaths.clear();
                visited.clear();
                rightSet.clear();
                path.push_back(_adjacencyList[s][j]);
                visited.insert(_adjacencyList[s][j]);
                nonOverlapPaths(path, visited, rightPaths, rightSet, t);
                count += bubblesFromLeftToRight(leftSet, rightSet, leftPaths,
                                                rightPaths);
            }
        }
        return count;
    }
};

int main(void)
{
    int k, t;
    std::string read;
    std::cin >> k >> t;
    DeBruijnGraph graph(k, t);
    while (std::cin >> read)
    {
        graph.addRead(read);
    }
    graph.constructDeBruijnGraph();
    std::cout << graph.totalBubbles() << std::endl;
    return 0;
}