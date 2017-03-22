# automatically generated by the FlatBuffers compiler, do not modify

# namespace: mmc

import flatbuffers

class UnitToCouples(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAsUnitToCouples(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = UnitToCouples()
        x.Init(buf, n + offset)
        return x

    # UnitToCouples
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # UnitToCouples
    def UnitId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, o + self._tab.Pos)
        return 0

    # UnitToCouples
    def ServicePrefix(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return ""

    # UnitToCouples
    def CoupleIds(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 4))
        return 0

    # UnitToCouples
    def CoupleIdsLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

def UnitToCouplesStart(builder): builder.StartObject(3)
def UnitToCouplesAddUnitId(builder, unitId): builder.PrependUint32Slot(0, unitId, 0)
def UnitToCouplesAddServicePrefix(builder, servicePrefix): builder.PrependUOffsetTRelativeSlot(1, flatbuffers.number_types.UOffsetTFlags.py_type(servicePrefix), 0)
def UnitToCouplesAddCoupleIds(builder, coupleIds): builder.PrependUOffsetTRelativeSlot(2, flatbuffers.number_types.UOffsetTFlags.py_type(coupleIds), 0)
def UnitToCouplesStartCoupleIdsVector(builder, numElems): return builder.StartVector(4, numElems, 4)
def UnitToCouplesEnd(builder): return builder.EndObject()