/** @file
  SSDT override that adds the missing _HID = "CIXH4010" to the three NPU core
  devices the MS-R1 BIOS exposes as \_SB.NPU0.CRE0, CRE1, CRE2.

  SPDX-License-Identifier: BSD-2-Clause-Patent
  Source: https://github.com/FyrbyAdditive/ms-r1-npu-hack
**/

DefinitionBlock ("ssdt-msr1-npu-core-hid.aml", "SSDT", 2, "MSR1", "NPUCRHID", 0x00000001)
{
  External (\_SB.NPU0,      DeviceObj)
  External (\_SB.NPU0.CRE0, DeviceObj)
  External (\_SB.NPU0.CRE1, DeviceObj)
  External (\_SB.NPU0.CRE2, DeviceObj)

  Scope (\_SB.NPU0.CRE0)
  {
    Name (_HID, "CIXH4010")
    Name (_UID, 0x0)
  }

  Scope (\_SB.NPU0.CRE1)
  {
    Name (_HID, "CIXH4010")
    Name (_UID, 0x1)
  }

  Scope (\_SB.NPU0.CRE2)
  {
    Name (_HID, "CIXH4010")
    Name (_UID, 0x2)
  }
}
