# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: mars_rover.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x10mars_rover.proto\x12\tmarsrover\"\x1d\n\x0c\x44riveRequest\x12\r\n\x05speed\x18\x01 \x01(\x02\"\r\n\x0bStopRequest\"6\n\x13MoveDistanceRequest\x12\x10\n\x08\x64istance\x18\x01 \x01(\x02\x12\r\n\x05speed\x18\x02 \x01(\x05\"\x1c\n\x0bTurnRequest\x12\r\n\x05speed\x18\x01 \x01(\x02\"\x1e\n\rRotateRequest\x12\r\n\x05speed\x18\x01 \x01(\x02\"0\n\x10TurnAngleRequest\x12\r\n\x05\x61ngle\x18\x01 \x01(\x02\x12\r\n\x05speed\x18\x02 \x01(\x05\"2\n\x12RotateAngleRequest\x12\r\n\x05\x61ngle\x18\x01 \x01(\x02\x12\r\n\x05speed\x18\x02 \x01(\x05\"I\n\x17ResourceObstacleRequest\x12\x10\n\x08\x64istance\x18\x01 \x01(\x02\x12\x0c\n\x04size\x18\x02 \x01(\x02\x12\x0e\n\x06object\x18\x03 \x01(\t\"3\n\x0f\x43ommandResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\x12\x0f\n\x07message\x18\x02 \x01(\t\"\x18\n\nLEDRequest\x12\n\n\x02on\x18\x01 \x01(\x08\"3\n\x0fWheelLEDRequest\x12\x14\n\x0cwheel_number\x18\x01 \x01(\x05\x12\n\n\x02on\x18\x02 \x01(\x08\"\x13\n\x11UltrasoundRequest\"&\n\x12UltrasoundResponse\x12\x10\n\x08\x64istance\x18\x01 \x01(\x02\"#\n\x0eSaveMapRequest\x12\x11\n\tfile_name\x18\x01 \x01(\t\"\x15\n\x13\x43\x61meraStreamRequest\"*\n\x14\x43\x61meraStreamResponse\x12\x12\n\nstream_url\x18\x01 \x01(\t\"\x0e\n\x0c\x45mptyRequest2\x8f\r\n\x0cRoverService\x12\x43\n\x0c\x44riveForward\x12\x17.marsrover.DriveRequest\x1a\x1a.marsrover.CommandResponse\x12>\n\x07Reverse\x12\x17.marsrover.DriveRequest\x1a\x1a.marsrover.CommandResponse\x12J\n\x0cMoveDistance\x12\x1e.marsrover.MoveDistanceRequest\x1a\x1a.marsrover.CommandResponse\x12>\n\x08TurnLeft\x12\x16.marsrover.TurnRequest\x1a\x1a.marsrover.CommandResponse\x12?\n\tTurnRight\x12\x16.marsrover.TurnRequest\x1a\x1a.marsrover.CommandResponse\x12@\n\nTurnOnSpot\x12\x16.marsrover.TurnRequest\x1a\x1a.marsrover.CommandResponse\x12\x44\n\tTurnAngle\x12\x1b.marsrover.TurnAngleRequest\x1a\x1a.marsrover.CommandResponse\x12\x46\n\tSpinAngle\x12\x1d.marsrover.RotateAngleRequest\x1a\x1a.marsrover.CommandResponse\x12K\n\x10TurnAngleForward\x12\x1b.marsrover.TurnAngleRequest\x1a\x1a.marsrover.CommandResponse\x12L\n\x11TurnAngleBackward\x12\x1b.marsrover.TurnAngleRequest\x1a\x1a.marsrover.CommandResponse\x12;\n\x05\x42rake\x12\x16.marsrover.StopRequest\x1a\x1a.marsrover.CommandResponse\x12\x42\n\x0cStopMovement\x12\x16.marsrover.StopRequest\x1a\x1a.marsrover.CommandResponse\x12G\n\x0fRotatePeriscope\x12\x18.marsrover.RotateRequest\x1a\x1a.marsrover.CommandResponse\x12\x46\n\x11\x43ontrolHeadlights\x12\x15.marsrover.LEDRequest\x1a\x1a.marsrover.CommandResponse\x12J\n\x10\x43ontrolWheelLEDs\x12\x1a.marsrover.WheelLEDRequest\x1a\x1a.marsrover.CommandResponse\x12M\n\x0bMapResource\x12\".marsrover.ResourceObstacleRequest\x1a\x1a.marsrover.CommandResponse\x12M\n\x0bMapObstacle\x12\".marsrover.ResourceObstacleRequest\x1a\x1a.marsrover.CommandResponse\x12I\n\x12ToggleResourceList\x12\x17.marsrover.EmptyRequest\x1a\x1a.marsrover.CommandResponse\x12I\n\x12ToggleObstacleList\x12\x17.marsrover.EmptyRequest\x1a\x1a.marsrover.CommandResponse\x12\x41\n\nToggleScan\x12\x17.marsrover.EmptyRequest\x1a\x1a.marsrover.CommandResponse\x12W\n\x18GetUltrasoundMeasurement\x12\x1c.marsrover.UltrasoundRequest\x1a\x1d.marsrover.UltrasoundResponse\x12@\n\x07SaveMap\x12\x19.marsrover.SaveMapRequest\x1a\x1a.marsrover.CommandResponse\x12R\n\x0fGetCameraStream\x12\x1e.marsrover.CameraStreamRequest\x1a\x1f.marsrover.CameraStreamResponseb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'mars_rover_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_DRIVEREQUEST']._serialized_start=31
  _globals['_DRIVEREQUEST']._serialized_end=60
  _globals['_STOPREQUEST']._serialized_start=62
  _globals['_STOPREQUEST']._serialized_end=75
  _globals['_MOVEDISTANCEREQUEST']._serialized_start=77
  _globals['_MOVEDISTANCEREQUEST']._serialized_end=131
  _globals['_TURNREQUEST']._serialized_start=133
  _globals['_TURNREQUEST']._serialized_end=161
  _globals['_ROTATEREQUEST']._serialized_start=163
  _globals['_ROTATEREQUEST']._serialized_end=193
  _globals['_TURNANGLEREQUEST']._serialized_start=195
  _globals['_TURNANGLEREQUEST']._serialized_end=243
  _globals['_ROTATEANGLEREQUEST']._serialized_start=245
  _globals['_ROTATEANGLEREQUEST']._serialized_end=295
  _globals['_RESOURCEOBSTACLEREQUEST']._serialized_start=297
  _globals['_RESOURCEOBSTACLEREQUEST']._serialized_end=370
  _globals['_COMMANDRESPONSE']._serialized_start=372
  _globals['_COMMANDRESPONSE']._serialized_end=423
  _globals['_LEDREQUEST']._serialized_start=425
  _globals['_LEDREQUEST']._serialized_end=449
  _globals['_WHEELLEDREQUEST']._serialized_start=451
  _globals['_WHEELLEDREQUEST']._serialized_end=502
  _globals['_ULTRASOUNDREQUEST']._serialized_start=504
  _globals['_ULTRASOUNDREQUEST']._serialized_end=523
  _globals['_ULTRASOUNDRESPONSE']._serialized_start=525
  _globals['_ULTRASOUNDRESPONSE']._serialized_end=563
  _globals['_SAVEMAPREQUEST']._serialized_start=565
  _globals['_SAVEMAPREQUEST']._serialized_end=600
  _globals['_CAMERASTREAMREQUEST']._serialized_start=602
  _globals['_CAMERASTREAMREQUEST']._serialized_end=623
  _globals['_CAMERASTREAMRESPONSE']._serialized_start=625
  _globals['_CAMERASTREAMRESPONSE']._serialized_end=667
  _globals['_EMPTYREQUEST']._serialized_start=669
  _globals['_EMPTYREQUEST']._serialized_end=683
  _globals['_ROVERSERVICE']._serialized_start=686
  _globals['_ROVERSERVICE']._serialized_end=2365
# @@protoc_insertion_point(module_scope)
