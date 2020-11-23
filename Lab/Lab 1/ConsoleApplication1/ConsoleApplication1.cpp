#include <iostream>
using namespace std;

#include "cpp_httplib/httplib.h"
#include "nlohmann/json.hpp"
using json = nlohmann::json;
using namespace httplib;
#include <ctime>
#include <iostream>
#include <iomanip>
#include <fstream>
#include <string>

Client cli("http://api.openweathermap.org");
string lat = "44.995890";
string long1 = "34.077394";
string exclude = "current,minutely,daily,alerts";
string lang = "ru";
string units = "metric";
string appid = "74d4bf42b15f53623d6fc846a3ed7584";

  
    void func_response(const Request& req, Response& res) {
        ofstream log("server.log", ofstream::app);
        log << "[log]" << ": gen_response began" << endl;
        string request = "/data/2.5/onecall?lat=" + lat + "&lon=" + long1 +
            "&exclude=" + exclude + "&appid=" + appid + "&units=" + units + "&lang=" + lang;

    