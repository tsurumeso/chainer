#pragma once

#include <memory>
#include <string>

#include "xchainer/backend.h"
#include "xchainer/device.h"

namespace xchainer {
namespace native {

class NativeDevice;
class NativeBackend;

namespace native_internal {

// Creates a device instance.
// This function is meant to be used from the backend class. Never use it for other purpose.
// This is defined in internal namespace in order to make it a friend of NativeDevice
// class.
NativeDevice* CreateDevice(NativeBackend& backend, int index);

}  // namespace native_internal

class NativeBackend : public Backend {
public:
    static constexpr const char* kDefaultName = "native";

    using Backend::Backend;

    std::string GetName() const override;

    int GetDeviceCount() const override;

    bool SupportsTransfer(Device& src_device, Device& dst_device) override;

private:
    std::unique_ptr<Device> CreateDevice(int index) override;
};

}  // namespace native
}  // namespace xchainer
