#include <bits/stdc++.h>
using namespace std;

// Without DIP
// High-level module depends directly on concrete classes

class TrendingRecommendationNoDIP
{
public:
    void recommend()
    {
        cout << "Trending Recommendations" << endl;
    }
};

class GenreRecommendationNoDIP
{
public:
    void recommend()
    {
        cout << "Genre Recommendations" << endl;
    }
};

class RecentRecommendationNoDIP
{
public:
    void recentRecommend()
    {
        cout << "Recent Recommendations" << endl;
    }
};

class RecommendationServiceNoDIP
{
public:
    void showTrending()
    {
        TrendingRecommendationNoDIP t;
        t.recommend();
    }

    void showGenre()
    {
        GenreRecommendationNoDIP g;
        g.recommend();
    }

    void showRecent()
    {
        RecentRecommendationNoDIP r;
        r.recentRecommend();
    }
};

// With DIP
// High-level module depends on abstraction instead of concrete classes

class RecommendationStrategy
{
public:
    virtual void recommend() = 0;
};

class TrendingRecommendation : public RecommendationStrategy
{
public:
    void recommend()
    {
        cout << "Trending Recommendations" << endl;
    }
};

class GenreRecommendation : public RecommendationStrategy
{
public:
    void recommend()
    {
        cout << "Genre Recommendations" << endl;
    }
};

class RecentRecommendation : public RecommendationStrategy
{
public:
    void recommend()
    {
        cout << "Recent Recommendations" << endl;
    }
};

class RecommendationService
{
private:
    RecommendationStrategy *strategy;

public:
    RecommendationService(RecommendationStrategy *strategy)
    {
        this->strategy = strategy;
    }

    void showRecommendations()
    {
        strategy->recommend();
    }
};

int main()
{
    cout << "----- WITHOUT DIP -----" << endl;

    RecommendationServiceNoDIP serviceNoDIP;
    serviceNoDIP.showTrending();
    serviceNoDIP.showGenre();
    serviceNoDIP.showRecent();

    cout << "----- WITH DIP -----" << endl;

    RecommendationStrategy *strategy = new TrendingRecommendation();
    RecommendationService service(strategy);

    service.showRecommendations();

    delete strategy;
    
    return 0;
}