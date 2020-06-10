# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from google.assistant.embedded.v1alpha2 import embedded_assistant_pb2 as google_dot_assistant_dot_embedded_dot_v1alpha2_dot_embedded__assistant__pb2


class EmbeddedAssistantStub(object):
  """Service that implements the Google Assistant API.
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.Assist = channel.stream_stream(
        '/google.assistant.embedded.v1alpha2.EmbeddedAssistant/Assist',
        request_serializer=google_dot_assistant_dot_embedded_dot_v1alpha2_dot_embedded__assistant__pb2.AssistRequest.SerializeToString,
        response_deserializer=google_dot_assistant_dot_embedded_dot_v1alpha2_dot_embedded__assistant__pb2.AssistResponse.FromString,
        )


class EmbeddedAssistantServicer(object):
  """Service that implements the Google Assistant API.
  """

  def Assist(self, request_iterator, context):
    """Initiates or continues a conversation with the embedded Assistant Service.
    Each call performs one round-trip, sending an audio request to the service
    and receiving the audio response. Uses bidirectional streaming to receive
    results, such as the `END_OF_UTTERANCE` event, while sending audio.

    A conversation is one or more gRPC connections, each consisting of several
    streamed requests and responses.
    For example, the user says *Add to my shopping list* and the Assistant
    responds *What do you want to add?*. The sequence of streamed requests and
    responses in the first gRPC message could be:

    *   AssistRequest.config
    *   AssistRequest.audio_in
    *   AssistRequest.audio_in
    *   AssistRequest.audio_in
    *   AssistRequest.audio_in
    *   AssistResponse.event_type.END_OF_UTTERANCE
    *   AssistResponse.speech_results.transcript "add to my shopping list"
    *   AssistResponse.dialog_state_out.microphone_mode.DIALOG_FOLLOW_ON
    *   AssistResponse.audio_out
    *   AssistResponse.audio_out
    *   AssistResponse.audio_out


    The user then says *bagels* and the Assistant responds
    *OK, I've added bagels to your shopping list*. This is sent as another gRPC
    connection call to the `Assist` method, again with streamed requests and
    responses, such as:

    *   AssistRequest.config
    *   AssistRequest.audio_in
    *   AssistRequest.audio_in
    *   AssistRequest.audio_in
    *   AssistResponse.event_type.END_OF_UTTERANCE
    *   AssistResponse.dialog_state_out.microphone_mode.CLOSE_MICROPHONE
    *   AssistResponse.audio_out
    *   AssistResponse.audio_out
    *   AssistResponse.audio_out
    *   AssistResponse.audio_out

    Although the precise order of responses is not guaranteed, sequential
    `AssistResponse.audio_out` messages will always contain sequential portions
    of audio.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_EmbeddedAssistantServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'Assist': grpc.stream_stream_rpc_method_handler(
          servicer.Assist,
          request_deserializer=google_dot_assistant_dot_embedded_dot_v1alpha2_dot_embedded__assistant__pb2.AssistRequest.FromString,
          response_serializer=google_dot_assistant_dot_embedded_dot_v1alpha2_dot_embedded__assistant__pb2.AssistResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'google.assistant.embedded.v1alpha2.EmbeddedAssistant', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
