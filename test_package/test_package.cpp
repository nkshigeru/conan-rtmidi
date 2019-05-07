#include <iostream>
#include <RtMidi.h>

int main() {
    std::cout << RtMidi::getVersion() << std::endl;
    std::vector<RtMidi::Api> apis;
    RtMidi::getCompiledApi(apis);
    for (auto api : apis)
    {
        std::cout << RtMidi::getApiName(api) << std::endl;
    }
}
