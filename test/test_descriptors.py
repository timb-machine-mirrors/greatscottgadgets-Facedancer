from facedancer import *
import unittest

# Test case similar to a game pad seen in the wild.

device_data = bytes([
    0x12, 0x01, 0x00, 0x02, 0x00, 0x00, 0x00, 0x40, 0x09,
    0x12, 0x05, 0x00, 0x00, 0x01, 0x01, 0x02, 0x00, 0x01])

strings = {
    1: "Facedancer Test",
    2: "Gamepad With Audio",
    4: "Interface 1",
    6: "Interface 3",
}

config_data = bytes([
    0x09, 0x02, 0xE3, 0x00, 0x04, 0x01, 0x03, 0xC0, 0xFA,
    0x09, 0x04, 0x00, 0x00, 0x00, 0x01, 0x01, 0x00, 0x04,
    0x0A, 0x24, 0x01, 0x00, 0x01, 0x49, 0x00, 0x02, 0x01, 0x02,
    0x0C, 0x24, 0x02, 0x01, 0x01, 0x01, 0x06, 0x04, 0x33, 0x00, 0x00, 0x00,
    0x0C, 0x24, 0x06, 0x02, 0x01, 0x01, 0x03, 0x00, 0x00, 0x00, 0x00, 0x00,
    0x09, 0x24, 0x03, 0x03, 0x01, 0x03, 0x04, 0x02, 0x00,
    0x0C, 0x24, 0x02, 0x04, 0x02, 0x04, 0x03, 0x02, 0x03, 0x00, 0x00, 0x00,
    0x09, 0x24, 0x06, 0x05, 0x04, 0x01, 0x03, 0x00, 0x00,
    0x09, 0x24, 0x03, 0x06, 0x01, 0x01, 0x01, 0x05, 0x00,
    0x09, 0x04, 0x01, 0x00, 0x00, 0x01, 0x02, 0x00, 0x00,
    0x09, 0x04, 0x01, 0x01, 0x01, 0x01, 0x02, 0x00, 0x00,
    0x07, 0x24, 0x01, 0x01, 0x01, 0x01, 0x00,
    0x0B, 0x24, 0x02, 0x01, 0x04, 0x02, 0x10, 0x01, 0x80, 0xBB, 0x00,
    0x09, 0x05, 0x01, 0x09, 0x88, 0x01, 0x04, 0x00, 0x00,
    0x07, 0x25, 0x01, 0x00, 0x00, 0x00, 0x00,
    0x09, 0x04, 0x02, 0x00, 0x00, 0x01, 0x02, 0x00, 0x00,
    0x09, 0x04, 0x02, 0x01, 0x01, 0x01, 0x02, 0x00, 0x00,
    0x07, 0x24, 0x01, 0x06, 0x01, 0x01, 0x00,
    0x0B, 0x24, 0x02, 0x01, 0x02, 0x02, 0x10, 0x01, 0x80, 0xBB, 0x00,
    0x09, 0x05, 0x82, 0x05, 0xC4, 0x00, 0x04, 0x00, 0x00,
    0x07, 0x25, 0x01, 0x00, 0x00, 0x00, 0x00,
    0x09, 0x04, 0x03, 0x00, 0x02, 0x03, 0x00, 0x00, 0x06,
    0x09, 0x21, 0x11, 0x01, 0x00, 0x01, 0x22, 0x11, 0x01,
    0x07, 0x05, 0x84, 0x03, 0x40, 0x00, 0x06,
    0x07, 0x05, 0x03, 0x03, 0x40, 0x00, 0x06,
])

report_data = bytes([
    0x05, 0x01, 0x09, 0x05, 0xA1, 0x01, 0x85, 0x01, 0x09, 0x30, 0x09, 0x31,
    0x09, 0x32, 0x09, 0x35, 0x09, 0x33, 0x09, 0x34, 0x15, 0x00, 0x26, 0xFF,
    0x00, 0x75, 0x08, 0x95, 0x06, 0x81, 0x02, 0x06, 0x00, 0xFF, 0x09, 0x20,
    0x95, 0x01, 0x81, 0x02, 0x05, 0x01, 0x09, 0x39, 0x15, 0x00, 0x25, 0x07,
    0x35, 0x00, 0x46, 0x3B, 0x01, 0x65, 0x14, 0x75, 0x04, 0x95, 0x01, 0x81,
    0x42, 0x65, 0x00, 0x05, 0x09, 0x19, 0x01, 0x29, 0x0F, 0x15, 0x00, 0x25,
    0x01, 0x75, 0x01, 0x95, 0x0F, 0x81, 0x02, 0x06, 0x00, 0xFF, 0x09, 0x21,
    0x95, 0x0D, 0x81, 0x02, 0x06, 0x00, 0xFF, 0x09, 0x22, 0x15, 0x00, 0x26,
    0xFF, 0x00, 0x75, 0x08, 0x95, 0x34, 0x81, 0x02, 0x85, 0x02, 0x09, 0x23,
    0x95, 0x2F, 0x91, 0x02, 0x85, 0x05, 0x09, 0x33, 0x95, 0x28, 0xB1, 0x02,
    0x85, 0x08, 0x09, 0x34, 0x95, 0x2F, 0xB1, 0x02, 0x85, 0x09, 0x09, 0x24,
    0x95, 0x13, 0xB1, 0x02, 0x85, 0x0A, 0x09, 0x25, 0x95, 0x1A, 0xB1, 0x02,
    0x85, 0x20, 0x09, 0x26, 0x95, 0x3F, 0xB1, 0x02, 0x85, 0x21, 0x09, 0x27,
    0x95, 0x04, 0xB1, 0x02, 0x85, 0x22, 0x09, 0x40, 0x95, 0x3F, 0xB1, 0x02,
    0x85, 0x80, 0x09, 0x28, 0x95, 0x3F, 0xB1, 0x02, 0x85, 0x81, 0x09, 0x29,
    0x95, 0x3F, 0xB1, 0x02, 0x85, 0x82, 0x09, 0x2A, 0x95, 0x09, 0xB1, 0x02,
    0x85, 0x83, 0x09, 0x2B, 0x95, 0x3F, 0xB1, 0x02, 0x85, 0x84, 0x09, 0x2C,
    0x95, 0x3F, 0xB1, 0x02, 0x85, 0x85, 0x09, 0x2D, 0x95, 0x02, 0xB1, 0x02,
    0x85, 0xA0, 0x09, 0x2E, 0x95, 0x01, 0xB1, 0x02, 0x85, 0xE0, 0x09, 0x2F,
    0x95, 0x3F, 0xB1, 0x02, 0x85, 0xF0, 0x09, 0x30, 0x95, 0x3F, 0xB1, 0x02,
    0x85, 0xF1, 0x09, 0x31, 0x95, 0x3F, 0xB1, 0x02, 0x85, 0xF2, 0x09, 0x32,
    0x95, 0x0F, 0xB1, 0x02, 0x85, 0xF4, 0x09, 0x35, 0x95, 0x3F, 0xB1, 0x02,
    0x85, 0xF5, 0x09, 0x36, 0x95, 0x03, 0xB1, 0x02, 0xC0
])

class TestDescriptors(unittest.TestCase):

    def test_device_descriptor_reconstruction(self):
        device = USBDevice.from_binary_descriptor(device_data)

        assert(device.get_descriptor() == device_data)

    def test_config_descriptor_reconstruction(self):
        configuration = USBConfiguration.from_binary_descriptor(config_data)

        device = USBDevice()
        device.add_configuration(configuration)

        assert(configuration.get_descriptor() == config_data)

    def test_code_generation(self):
        # Construct a device from binary descriptors.
        device = USBDevice.from_binary_descriptor(device_data, strings)
        configuration = USBConfiguration.from_binary_descriptor(config_data, strings)
        device.add_configuration(configuration)
        report_desc = USBDescriptor(type_number=0x22, number=0, raw=report_data)
        hid_interface = configuration.interfaces[(3, 0)]
        hid_interface.add_descriptor(report_desc)

        # Generate code and check it matches expected output.
        code = device.generate_code()
        self.maxDiff = None
        self.assertEqual(expected_code, code)

        # Run that code and check that it generates the matching descriptors.
        exec(code, globals())
        new_device = Device()
        self.assertEqual(new_device.get_descriptor(), device_data)
        new_config = new_device.configurations[1]
        self.assertEqual(new_config.get_descriptor(), config_data)
        new_hid_interface = new_config.interfaces[(3, 0)]
        new_report_desc = new_hid_interface.requestable_descriptors[(0x22, 0)]
        self.assertEqual(new_report_desc.raw, report_data)

        # Check that it also produces the same code again.
        new_code = new_device.generate_code()
        self.assertEqual(expected_code, new_code)

expected_code = """
@use_inner_classes_automatically
class Device(USBDevice):
    device_speed             = None
    device_class             = 0
    device_subclass          = 0
    protocol_revision_number = 0
    max_packet_size_ep0      = 64
    vendor_id                = 0x1209
    product_id               = 0x0005
    manufacturer_string      = (1, 'Facedancer Test')
    product_string           = (2, 'Gamepad With Audio')
    serial_number_string     = None
    supported_languages      = (LanguageIDs.ENGLISH_US,)
    device_revision          = 0x0100
    usb_spec_version         = 0x0200

    class Configuration_1(USBConfiguration):
        number                 = 1
        configuration_string   = 3
        max_power              = 500
        self_powered           = True
        supports_remote_wakeup = False

        class Interface_0(USBInterface):
            number           = 0
            alternate        = 0
            class_number     = 1
            subclass_number  = 1
            protocol_number  = 0
            interface_string = (4, 'Interface 1')

            @include_in_config
            class Descriptor_0x24_A(USBDescriptor):
                raw = bytes([
                    0x0A, 0x24, 0x01, 0x00, 0x01,
                    0x49, 0x00, 0x02, 0x01, 0x02])

            @include_in_config
            class Descriptor_0x24_B(USBDescriptor):
                raw = bytes([
                    0x0C, 0x24, 0x02, 0x01, 0x01, 0x01,
                    0x06, 0x04, 0x33, 0x00, 0x00, 0x00])

            @include_in_config
            class Descriptor_0x24_C(USBDescriptor):
                raw = bytes([
                    0x0C, 0x24, 0x06, 0x02, 0x01, 0x01,
                    0x03, 0x00, 0x00, 0x00, 0x00, 0x00])

            @include_in_config
            class Descriptor_0x24_D(USBDescriptor):
                raw = bytes([
                    0x09, 0x24, 0x03, 0x03, 0x01,
                    0x03, 0x04, 0x02, 0x00])

            @include_in_config
            class Descriptor_0x24_E(USBDescriptor):
                raw = bytes([
                    0x0C, 0x24, 0x02, 0x04, 0x02, 0x04,
                    0x03, 0x02, 0x03, 0x00, 0x00, 0x00])

            @include_in_config
            class Descriptor_0x24_F(USBDescriptor):
                raw = bytes([
                    0x09, 0x24, 0x06, 0x05, 0x04,
                    0x01, 0x03, 0x00, 0x00])

            @include_in_config
            class Descriptor_0x24_G(USBDescriptor):
                raw = bytes([
                    0x09, 0x24, 0x03, 0x06, 0x01,
                    0x01, 0x01, 0x05, 0x00])

        class Interface_1(USBInterface):
            number           = 1
            alternate        = 0
            class_number     = 1
            subclass_number  = 2
            protocol_number  = 0
            interface_string = None

        class Interface_1_1(USBInterface):
            number           = 1
            alternate        = 1
            class_number     = 1
            subclass_number  = 2
            protocol_number  = 0
            interface_string = None

            @include_in_config
            class Descriptor_0x24_A(USBDescriptor):
                raw = bytes([
                    0x07, 0x24, 0x01, 0x01, 0x01, 0x01, 0x00])

            @include_in_config
            class Descriptor_0x24_B(USBDescriptor):
                raw = bytes([
                    0x0B, 0x24, 0x02, 0x01, 0x04, 0x02,
                    0x10, 0x01, 0x80, 0xBB, 0x00])

            class Endpoint_1_OUT(USBEndpoint):
                number               = 1
                direction            = USBDirection.OUT
                transfer_type        = USBTransferType.ISOCHRONOUS
                synchronization_type = USBSynchronizationType.ADAPTIVE
                usage_type           = USBUsageType.DATA
                max_packet_size      = 392
                interval             = 4
                extra_bytes          = bytes([0x00, 0x00])

                @include_in_config
                class Descriptor_0x25_A(USBDescriptor):
                    raw = bytes([
                        0x07, 0x25, 0x01, 0x00, 0x00, 0x00, 0x00])

        class Interface_2(USBInterface):
            number           = 2
            alternate        = 0
            class_number     = 1
            subclass_number  = 2
            protocol_number  = 0
            interface_string = None

        class Interface_2_1(USBInterface):
            number           = 2
            alternate        = 1
            class_number     = 1
            subclass_number  = 2
            protocol_number  = 0
            interface_string = None

            @include_in_config
            class Descriptor_0x24_A(USBDescriptor):
                raw = bytes([
                    0x07, 0x24, 0x01, 0x06, 0x01, 0x01, 0x00])

            @include_in_config
            class Descriptor_0x24_B(USBDescriptor):
                raw = bytes([
                    0x0B, 0x24, 0x02, 0x01, 0x02, 0x02,
                    0x10, 0x01, 0x80, 0xBB, 0x00])

            class Endpoint_2_IN(USBEndpoint):
                number               = 2
                direction            = USBDirection.IN
                transfer_type        = USBTransferType.ISOCHRONOUS
                synchronization_type = USBSynchronizationType.ASYNC
                usage_type           = USBUsageType.DATA
                max_packet_size      = 196
                interval             = 4
                extra_bytes          = bytes([0x00, 0x00])

                @include_in_config
                class Descriptor_0x25_A(USBDescriptor):
                    raw = bytes([
                        0x07, 0x25, 0x01, 0x00, 0x00, 0x00, 0x00])

        class Interface_3(USBInterface):
            number           = 3
            alternate        = 0
            class_number     = 3
            subclass_number  = 0
            protocol_number  = 0
            interface_string = (6, 'Interface 3')

            @include_in_config
            class Descriptor_0x21_A(USBDescriptor):
                raw = bytes([
                    0x09, 0x21, 0x11, 0x01, 0x00,
                    0x01, 0x22, 0x11, 0x01])

            class Endpoint_4_IN(USBEndpoint):
                number               = 4
                direction            = USBDirection.IN
                transfer_type        = USBTransferType.INTERRUPT
                synchronization_type = USBSynchronizationType.NONE
                usage_type           = USBUsageType.DATA
                max_packet_size      = 64
                interval             = 6
                extra_bytes          = bytes([])

            class Endpoint_3_OUT(USBEndpoint):
                number               = 3
                direction            = USBDirection.OUT
                transfer_type        = USBTransferType.INTERRUPT
                synchronization_type = USBSynchronizationType.NONE
                usage_type           = USBUsageType.DATA
                max_packet_size      = 64
                interval             = 6
                extra_bytes          = bytes([])

            @requestable(type_number=0x22, number=0)
            class Descriptor_0x22_0(USBDescriptor):
                raw = bytes([
                    0x05, 0x01, 0x09, 0x05, 0xA1, 0x01, 0x85, 0x01, 0x09, 0x30,
                    0x09, 0x31, 0x09, 0x32, 0x09, 0x35, 0x09, 0x33, 0x09, 0x34,
                    0x15, 0x00, 0x26, 0xFF, 0x00, 0x75, 0x08, 0x95, 0x06, 0x81,
                    0x02, 0x06, 0x00, 0xFF, 0x09, 0x20, 0x95, 0x01, 0x81, 0x02,
                    0x05, 0x01, 0x09, 0x39, 0x15, 0x00, 0x25, 0x07, 0x35, 0x00,
                    0x46, 0x3B, 0x01, 0x65, 0x14, 0x75, 0x04, 0x95, 0x01, 0x81,
                    0x42, 0x65, 0x00, 0x05, 0x09, 0x19, 0x01, 0x29, 0x0F, 0x15,
                    0x00, 0x25, 0x01, 0x75, 0x01, 0x95, 0x0F, 0x81, 0x02, 0x06,
                    0x00, 0xFF, 0x09, 0x21, 0x95, 0x0D, 0x81, 0x02, 0x06, 0x00,
                    0xFF, 0x09, 0x22, 0x15, 0x00, 0x26, 0xFF, 0x00, 0x75, 0x08,
                    0x95, 0x34, 0x81, 0x02, 0x85, 0x02, 0x09, 0x23, 0x95, 0x2F,
                    0x91, 0x02, 0x85, 0x05, 0x09, 0x33, 0x95, 0x28, 0xB1, 0x02,
                    0x85, 0x08, 0x09, 0x34, 0x95, 0x2F, 0xB1, 0x02, 0x85, 0x09,
                    0x09, 0x24, 0x95, 0x13, 0xB1, 0x02, 0x85, 0x0A, 0x09, 0x25,
                    0x95, 0x1A, 0xB1, 0x02, 0x85, 0x20, 0x09, 0x26, 0x95, 0x3F,
                    0xB1, 0x02, 0x85, 0x21, 0x09, 0x27, 0x95, 0x04, 0xB1, 0x02,
                    0x85, 0x22, 0x09, 0x40, 0x95, 0x3F, 0xB1, 0x02, 0x85, 0x80,
                    0x09, 0x28, 0x95, 0x3F, 0xB1, 0x02, 0x85, 0x81, 0x09, 0x29,
                    0x95, 0x3F, 0xB1, 0x02, 0x85, 0x82, 0x09, 0x2A, 0x95, 0x09,
                    0xB1, 0x02, 0x85, 0x83, 0x09, 0x2B, 0x95, 0x3F, 0xB1, 0x02,
                    0x85, 0x84, 0x09, 0x2C, 0x95, 0x3F, 0xB1, 0x02, 0x85, 0x85,
                    0x09, 0x2D, 0x95, 0x02, 0xB1, 0x02, 0x85, 0xA0, 0x09, 0x2E,
                    0x95, 0x01, 0xB1, 0x02, 0x85, 0xE0, 0x09, 0x2F, 0x95, 0x3F,
                    0xB1, 0x02, 0x85, 0xF0, 0x09, 0x30, 0x95, 0x3F, 0xB1, 0x02,
                    0x85, 0xF1, 0x09, 0x31, 0x95, 0x3F, 0xB1, 0x02, 0x85, 0xF2,
                    0x09, 0x32, 0x95, 0x0F, 0xB1, 0x02, 0x85, 0xF4, 0x09, 0x35,
                    0x95, 0x3F, 0xB1, 0x02, 0x85, 0xF5, 0x09, 0x36, 0x95, 0x03,
                    0xB1, 0x02, 0xC0])
"""

if __name__ == "__main__":
    unittest.main()
