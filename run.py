#! /usr/local/bin/python3.8

from prometheus_client import start_http_server
from prometheus_client.core import GaugeMetricFamily, REGISTRY
import json
import asyncio
import time
from os import environ
import requests
from requests.exceptions import Timeout


async def get_json(host):
    try:
        response = requests.get(host + '/colibri/stats', timeout=1)
        response_json = json.loads(response.text)
        return response_json
    except Timeout:
        print(host + ': timeout')
        return 'error'


async def build_json(hosts: tuple):
    data = dict()
    for host in hosts:
        meeting = asyncio.create_task(get_json(f'http://{host}:8080'))

        await meeting,
        data[host] = meeting.result()

    return data


class CustomCollector:
    def __init__(self, hosts: tuple = None):
        self.hosts = hosts

    def collect(self):
        data = asyncio.run(build_json(self.hosts))
        print(data)

        inactive_endpoints = GaugeMetricFamily("inactive_endpoints", "inactive_endpoints", labels=["instance"])
        for host in self.hosts:
            if data[host] != "error":
                inactive_endpoints.add_metric([host.split(".")[0]], data[host]["inactive_endpoints"])
        yield inactive_endpoints

        inactive_conferences = GaugeMetricFamily("inactive_conferences", "inactive_conferences", labels=["instance"])
        for host in self.hosts:
            if data[host] != "error":
                inactive_conferences.add_metric([host.split(".")[0]], data[host]["inactive_conferences"])
        yield inactive_conferences

        total_ice_succeeded_relayed = GaugeMetricFamily("total_ice_succeeded_relayed", "total_ice_succeeded_relayed",
                                                        labels=["instance"])
        for host in self.hosts:
            if data[host] != "error":
                total_ice_succeeded_relayed.add_metric([host.split(".")[0]], data[host]["total_ice_succeeded_relayed"])
        yield total_ice_succeeded_relayed

        total_loss_degraded_participant_seconds = GaugeMetricFamily("total_loss_degraded_participant_seconds",
                                                                    "total_loss_degraded_participant_seconds",
                                                                    labels=["instance"])
        for host in self.hosts:
            if data[host] != "error":
                total_loss_degraded_participant_seconds.add_metric([host.split(".")[0]], data[host][
                    "total_loss_degraded_participant_seconds"])
        yield total_loss_degraded_participant_seconds

        bit_rate_download = GaugeMetricFamily("bit_rate_download", "bit_rate_download", labels=["instance"])
        for host in self.hosts:
            if data[host] != "error":
                bit_rate_download.add_metric([host.split(".")[0]], data[host]["bit_rate_download"])
        yield bit_rate_download

        muc_clients_connected = GaugeMetricFamily("muc_clients_connected", "muc_clients_connected", labels=["instance"])
        for host in self.hosts:
            if data[host] != "error":
                muc_clients_connected.add_metric([host.split(".")[0]], data[host]["muc_clients_connected"])
        yield muc_clients_connected

        total_participants = GaugeMetricFamily("total_participants", "total_participants", labels=["instance"])
        for host in self.hosts:
            if data[host] != "error":
                total_participants.add_metric([host.split(".")[0]], data[host]["total_participants"])
        yield total_participants

        total_packets_received = GaugeMetricFamily("total_packets_received", "total_packets_received",
                                                   labels=["instance"])
        for host in self.hosts:
            if data[host] != "error":
                total_packets_received.add_metric([host.split(".")[0]], data[host]["total_packets_received"])
        yield total_packets_received

        rtt_aggregate = GaugeMetricFamily("rtt_aggregate", "rtt_aggregate", labels=["instance"])
        for host in self.hosts:
            if data[host] != "error":
                rtt_aggregate.add_metric([host.split(".")[0]], data[host]["rtt_aggregate"])
        yield rtt_aggregate

        packet_rate_upload = GaugeMetricFamily("packet_rate_upload", "packet_rate_upload", labels=["instance"])
        for host in self.hosts:
            if data[host] != "error":
                packet_rate_upload.add_metric([host.split(".")[0]], data[host]["packet_rate_upload"])
        yield packet_rate_upload

        p2p_conferences = GaugeMetricFamily("p2p_conferences", "p2p_conferences", labels=["instance"])
        for host in self.hosts:
            if data[host] != "error":
                p2p_conferences.add_metric([host.split(".")[0]], data[host]["p2p_conferences"])
        yield p2p_conferences

        total_loss_limited_participant_seconds = GaugeMetricFamily("total_loss_limited_participant_seconds",
                                                                   "total_loss_limited_participant_seconds",
                                                                   labels=["instance"])
        for host in self.hosts:
            if data[host] != "error":
                total_loss_limited_participant_seconds.add_metric([host.split(".")[0]],
                                                                  data[host]["total_loss_limited_participant_seconds"])
        yield total_loss_limited_participant_seconds

        octo_send_bitrate = GaugeMetricFamily("octo_send_bitrate", "octo_send_bitrate", labels=["instance"])
        for host in self.hosts:
            if data[host] != "error":
                octo_send_bitrate.add_metric([host.split(".")[0]], data[host]["octo_send_bitrate"])
        yield octo_send_bitrate

        total_dominant_speaker_changes = GaugeMetricFamily("total_dominant_speaker_changes",
                                                           "total_dominant_speaker_changes", labels=["instance"])
        for host in self.hosts:
            if data[host] != "error":
                total_dominant_speaker_changes.add_metric([host.split(".")[0]],
                                                          data[host]["total_dominant_speaker_changes"])
        yield total_dominant_speaker_changes

        receive_only_endpoints = GaugeMetricFamily("receive_only_endpoints", "receive_only_endpoints",
                                                   labels=["instance"])
        for host in self.hosts:
            if data[host] != "error":
                receive_only_endpoints.add_metric([host.split(".")[0]], data[host]["receive_only_endpoints"])
        yield receive_only_endpoints

        total_colibri_web_socket_messages_received = GaugeMetricFamily("total_colibri_web_socket_messages_received",
                                                                       "total_colibri_web_socket_messages_received",
                                                                       labels=["instance"])
        for host in self.hosts:
            if data[host] != "error":
                total_colibri_web_socket_messages_received.add_metric([host.split(".")[0]], data[host][
                    "total_colibri_web_socket_messages_received"])
        yield total_colibri_web_socket_messages_received

        octo_receive_bitrate = GaugeMetricFamily("octo_receive_bitrate", "octo_receive_bitrate", labels=["instance"])
        for host in self.hosts:
            if data[host] != "error":
                octo_receive_bitrate.add_metric([host.split(".")[0]], data[host]["octo_receive_bitrate"])
        yield octo_receive_bitrate

        #loss_rate_upload = GaugeMetricFamily("loss_rate_upload", "loss_rate_upload", labels=["instance"])
        #for host in self.hosts:
        #    if data[host] != "error":
        #        loss_rate_upload.add_metric([host.split(".")[0]], data[host]["loss_rate_upload"])
        #yield loss_rate_upload

        total_ice_succeeded = GaugeMetricFamily("total_ice_succeeded", "total_ice_succeeded", labels=["instance"])
        for host in self.hosts:
            if data[host] != "error":
                total_ice_succeeded.add_metric([host.split(".")[0]], data[host]["total_ice_succeeded"])
        yield total_ice_succeeded

        total_colibri_web_socket_messages_sent = GaugeMetricFamily("total_colibri_web_socket_messages_sent",
                                                                   "total_colibri_web_socket_messages_sent",
                                                                   labels=["instance"])
        for host in self.hosts:
            if data[host] != "error":
                total_colibri_web_socket_messages_sent.add_metric([host.split(".")[0]],
                                                                  data[host]["total_colibri_web_socket_messages_sent"])
        yield total_colibri_web_socket_messages_sent

        total_bytes_sent_octo = GaugeMetricFamily("total_bytes_sent_octo", "total_bytes_sent_octo", labels=["instance"])
        for host in self.hosts:
            if data[host] != "error":
                total_bytes_sent_octo.add_metric([host.split(".")[0]], data[host]["total_bytes_sent_octo"])
        yield total_bytes_sent_octo

        total_data_channel_messages_received = GaugeMetricFamily("total_data_channel_messages_received",
                                                                 "total_data_channel_messages_received",
                                                                 labels=["instance"])
        for host in self.hosts:
            if data[host] != "error":
                total_data_channel_messages_received.add_metric([host.split(".")[0]],
                                                                data[host]["total_data_channel_messages_received"])
        yield total_data_channel_messages_received

        #loss_rate_download = GaugeMetricFamily("loss_rate_download", "loss_rate_download", labels=["instance"])
        #for host in self.hosts:
        #    if data[host] != "error":
        #        loss_rate_download.add_metric([host.split(".")[0]], data[host]["loss_rate_download"])
        #yield loss_rate_download

        total_conference_seconds = GaugeMetricFamily("total_conference_seconds", "total_conference_seconds",
                                                     labels=["instance"])
        for host in self.hosts:
            if data[host] != "error":
                total_conference_seconds.add_metric([host.split(".")[0]], data[host]["total_conference_seconds"])
        yield total_conference_seconds

        bit_rate_upload = GaugeMetricFamily("bit_rate_upload", "bit_rate_upload", labels=["instance"])
        for host in self.hosts:
            if data[host] != "error":
                bit_rate_upload.add_metric([host.split(".")[0]], data[host]["bit_rate_upload"])
        yield bit_rate_upload

        total_conferences_completed = GaugeMetricFamily("total_conferences_completed", "total_conferences_completed",
                                                        labels=["instance"])
        for host in self.hosts:
            if data[host] != "error":
                total_conferences_completed.add_metric([host.split(".")[0]], data[host]["total_conferences_completed"])
        yield total_conferences_completed

        octo_conferences = GaugeMetricFamily("octo_conferences", "octo_conferences", labels=["instance"])
        for host in self.hosts:
            if data[host] != "error":
                octo_conferences.add_metric([host.split(".")[0]], data[host]["octo_conferences"])
        yield octo_conferences

        num_eps_no_msg_transport_after_delay = GaugeMetricFamily("num_eps_no_msg_transport_after_delay",
                                                                 "num_eps_no_msg_transport_after_delay",
                                                                 labels=["instance"])
        for host in self.hosts:
            if data[host] != "error":
                num_eps_no_msg_transport_after_delay.add_metric([host.split(".")[0]],
                                                                data[host]["num_eps_no_msg_transport_after_delay"])
        yield num_eps_no_msg_transport_after_delay

        endpoints_sending_video = GaugeMetricFamily("endpoints_sending_video", "endpoints_sending_video",
                                                    labels=["instance"])
        for host in self.hosts:
            if data[host] != "error":
                endpoints_sending_video.add_metric([host.split(".")[0]], data[host]["endpoints_sending_video"])
        yield endpoints_sending_video

        packet_rate_download = GaugeMetricFamily("packet_rate_download", "packet_rate_download", labels=["instance"])
        for host in self.hosts:
            if data[host] != "error":
                packet_rate_download.add_metric([host.split(".")[0]], data[host]["packet_rate_download"])
        yield packet_rate_download

        muc_clients_configured = GaugeMetricFamily("muc_clients_configured", "muc_clients_configured",
                                                   labels=["instance"])
        for host in self.hosts:
            if data[host] != "error":
                muc_clients_configured.add_metric([host.split(".")[0]], data[host]["muc_clients_configured"])
        yield muc_clients_configured

        total_packets_sent_octo = GaugeMetricFamily("total_packets_sent_octo", "total_packets_sent_octo",
                                                    labels=["instance"])
        for host in self.hosts:
            if data[host] != "error":
                total_packets_sent_octo.add_metric([host.split(".")[0]], data[host]["total_packets_sent_octo"])
        yield total_packets_sent_octo

        #videostreams = GaugeMetricFamily("videostreams", "videostreams", labels=["instance"])
        #for host in self.hosts:
        #    if data[host] != "error":
        #        videostreams.add_metric([host.split(".")[0]], data[host]["videostreams"])
        #yield videostreams

        jitter_aggregate = GaugeMetricFamily("jitter_aggregate", "jitter_aggregate", labels=["instance"])
        for host in self.hosts:
            if data[host] != "error":
                jitter_aggregate.add_metric([host.split(".")[0]], data[host]["jitter_aggregate"])
        yield jitter_aggregate

        total_ice_succeeded_tcp = GaugeMetricFamily("total_ice_succeeded_tcp", "total_ice_succeeded_tcp",
                                                    labels=["instance"])
        for host in self.hosts:
            if data[host] != "error":
                total_ice_succeeded_tcp.add_metric([host.split(".")[0]], data[host]["total_ice_succeeded_tcp"])
        yield total_ice_succeeded_tcp

        octo_endpoints = GaugeMetricFamily("octo_endpoints", "octo_endpoints", labels=["instance"])
        for host in self.hosts:
            if data[host] != "error":
                octo_endpoints.add_metric([host.split(".")[0]], data[host]["octo_endpoints"])
        yield octo_endpoints

        total_packets_dropped_octo = GaugeMetricFamily("total_packets_dropped_octo", "total_packets_dropped_octo",
                                                       labels=["instance"])
        for host in self.hosts:
            if data[host] != "error":
                total_packets_dropped_octo.add_metric([host.split(".")[0]], data[host]["total_packets_dropped_octo"])
        yield total_packets_dropped_octo

        conferences = GaugeMetricFamily("conferences", "conferences", labels=["instance"])
        for host in self.hosts:
            if data[host] != "error":
                conferences.add_metric([host.split(".")[0]], data[host]["conferences"])
        yield conferences

        participants = GaugeMetricFamily("participants", "participants", labels=["instance"])
        for host in self.hosts:
            if data[host] != "error":
                participants.add_metric([host.split(".")[0]], data[host]["participants"])
        yield participants

        largest_conference = GaugeMetricFamily("largest_conference", "largest_conference", labels=["instance"])
        for host in self.hosts:
            if data[host] != "error":
                largest_conference.add_metric([host.split(".")[0]], data[host]["largest_conference"])
        yield largest_conference

        total_packets_sent = GaugeMetricFamily("total_packets_sent", "total_packets_sent", labels=["instance"])
        for host in self.hosts:
            if data[host] != "error":
                total_packets_sent.add_metric([host.split(".")[0]], data[host]["total_packets_sent"])
        yield total_packets_sent

        total_data_channel_messages_sent = GaugeMetricFamily("total_data_channel_messages_sent",
                                                             "total_data_channel_messages_sent", labels=["instance"])
        for host in self.hosts:
            if data[host] != "error":
                total_data_channel_messages_sent.add_metric([host.split(".")[0]],
                                                            data[host]["total_data_channel_messages_sent"])
        yield total_data_channel_messages_sent

        total_bytes_received_octo = GaugeMetricFamily("total_bytes_received_octo", "total_bytes_received_octo",
                                                      labels=["instance"])
        for host in self.hosts:
            if data[host] != "error":
                total_bytes_received_octo.add_metric([host.split(".")[0]], data[host]["total_bytes_received_octo"])
        yield total_bytes_received_octo

        octo_send_packet_rate = GaugeMetricFamily("octo_send_packet_rate", "octo_send_packet_rate", labels=["instance"])
        for host in self.hosts:
            if data[host] != "error":
                octo_send_packet_rate.add_metric([host.split(".")[0]], data[host]["octo_send_packet_rate"])
        yield octo_send_packet_rate

        total_conferences_created = GaugeMetricFamily("total_conferences_created", "total_conferences_created",
                                                      labels=["instance"])
        for host in self.hosts:
            if data[host] != "error":
                total_conferences_created.add_metric([host.split(".")[0]], data[host]["total_conferences_created"])
        yield total_conferences_created

        total_ice_failed = GaugeMetricFamily("total_ice_failed", "total_ice_failed", labels=["instance"])
        for host in self.hosts:
            if data[host] != "error":
                total_ice_failed.add_metric([host.split(".")[0]], data[host]["total_ice_failed"])
        yield total_ice_failed

        threads = GaugeMetricFamily("threads", "threads", labels=["instance"])
        for host in self.hosts:
            if data[host] != "error":
                threads.add_metric([host.split(".")[0]], data[host]["threads"])
        yield threads

        videochannels = GaugeMetricFamily("videochannels", "videochannels", labels=["instance"])
        for host in self.hosts:
            if data[host] != "error":
                videochannels.add_metric([host.split(".")[0]], data[host]["videochannels"])
        yield videochannels

        total_packets_received_octo = GaugeMetricFamily("total_packets_received_octo", "total_packets_received_octo",
                                                        labels=["instance"])
        for host in self.hosts:
            if data[host] != "error":
                total_packets_received_octo.add_metric([host.split(".")[0]], data[host]["total_packets_received_octo"])
        yield total_packets_received_octo

        octo_receive_packet_rate = GaugeMetricFamily("octo_receive_packet_rate", "octo_receive_packet_rate",
                                                     labels=["instance"])
        for host in self.hosts:
            if data[host] != "error":
                octo_receive_packet_rate.add_metric([host.split(".")[0]], data[host]["octo_receive_packet_rate"])
        yield octo_receive_packet_rate

        total_bytes_received = GaugeMetricFamily("total_bytes_received", "total_bytes_received", labels=["instance"])
        for host in self.hosts:
            if data[host] != "error":
                total_bytes_received.add_metric([host.split(".")[0]], data[host]["total_bytes_received"])
        yield total_bytes_received

        #rtp_loss = GaugeMetricFamily("rtp_loss", "rtp_loss", labels=["instance"])
        #for host in self.hosts:
        #    if data[host] != "error":
        #        rtp_loss.add_metric([host.split(".")[0]], data[host]["rtp_loss"])
        #yield rtp_loss

        total_loss_controlled_participant_seconds = GaugeMetricFamily("total_loss_controlled_participant_seconds",
                                                                      "total_loss_controlled_participant_seconds",
                                                                      labels=["instance"])
        for host in self.hosts:
            if data[host] != "error":
                total_loss_controlled_participant_seconds.add_metric([host.split(".")[0]], data[host][
                    "total_loss_controlled_participant_seconds"])
        yield total_loss_controlled_participant_seconds

        total_partially_failed_conferences = GaugeMetricFamily("total_partially_failed_conferences",
                                                               "total_partially_failed_conferences",
                                                               labels=["instance"])
        for host in self.hosts:
            if data[host] != "error":
                total_partially_failed_conferences.add_metric([host.split(".")[0]],
                                                              data[host]["total_partially_failed_conferences"])
        yield total_partially_failed_conferences

        endpoints_sending_audio = GaugeMetricFamily("endpoints_sending_audio", "endpoints_sending_audio",
                                                    labels=["instance"])
        for host in self.hosts:
            if data[host] != "error":
                endpoints_sending_audio.add_metric([host.split(".")[0]], data[host]["endpoints_sending_audio"])
        yield endpoints_sending_audio

        total_bytes_sent = GaugeMetricFamily("total_bytes_sent", "total_bytes_sent", labels=["instance"])
        for host in self.hosts:
            if data[host] != "error":
                total_bytes_sent.add_metric([host.split(".")[0]], data[host]["total_bytes_sent"])
        yield total_bytes_sent

        mucs_configured = GaugeMetricFamily("mucs_configured", "mucs_configured", labels=["instance"])
        for host in self.hosts:
            if data[host] != "error":
                mucs_configured.add_metric([host.split(".")[0]], data[host]["mucs_configured"])
        yield mucs_configured

        total_failed_conferences = GaugeMetricFamily("total_failed_conferences", "total_failed_conferences",
                                                     labels=["instance"])
        for host in self.hosts:
            if data[host] != "error":
                total_failed_conferences.add_metric([host.split(".")[0]], data[host]["total_failed_conferences"])
        yield total_failed_conferences

        mucs_joined = GaugeMetricFamily("mucs_joined", "mucs_joined", labels=["instance"])
        for host in self.hosts:
            if data[host] != "error":
                mucs_joined.add_metric([host.split(".")[0]], data[host]["mucs_joined"])
        yield mucs_joined

        version = GaugeMetricFamily("version", "version", labels=["instance", "version"])
        for host in self.hosts:
            if data[host] != "error":
                version.add_metric([host.split(".")[0], data[host]["version"]], 0)
        yield version

        current_timestamp = GaugeMetricFamily("current_timestamp", "current_timestamp",
                                              labels=["instance", "current_timestamp"])
        for host in self.hosts:
            if data[host] != "error":
                current_timestamp.add_metric([host.split(".")[0], data[host]["current_timestamp"]], 0)
        yield current_timestamp

        graceful_shutdown = GaugeMetricFamily("graceful_shutdown", "graceful_shutdown", labels=["instance"])
        for host in self.hosts:
            if data[host] != "error":
                if data[host]["graceful_shutdown"]:
                    graceful_shutdown.add_metric([host.split(".")[0]], 1)
                else:
                    graceful_shutdown.add_metric([host.split(".")[0]], 0)
        yield graceful_shutdown

        conference_sizes = GaugeMetricFamily("conference_sizes", "conference_sizes", labels=["instance", "le"])
        for host in self.hosts:
            if data[host] != "error":
                for le in range(0, 22):
                    conference_sizes.add_metric([host.split(".")[0], str(le)], data[host]["conference_sizes"][le])
        yield conference_sizes

        conferences_by_video_senders = GaugeMetricFamily(
            "conferences_by_video_senders",
            "conferences_by_video_senders",
            labels=["instance", "le"]
        )
        for host in self.hosts:
            if data[host] != "error":
                for le in range(0, 22):
                    conferences_by_video_senders.add_metric(
                        [host.split(".")[0], str(le)],
                        data[host]["conferences_by_video_senders"][le]
                    )
        yield conferences_by_video_senders

        conferences_by_audio_senders = GaugeMetricFamily(
            "conferences_by_audio_senders",
            "conferences_by_audio_senders",
            labels=["instance", "le"]
        )
        for host in self.hosts:
            if data[host] != "error":
                for le in range(0, 22):
                    conferences_by_audio_senders.add_metric(
                        [host.split(".")[0], str(le)],
                        data[host]["conferences_by_audio_senders"][le]
                    )
        yield conferences_by_audio_senders


if __name__ == '__main__':
    start_http_server(int(environ.get('HTTP_PORT', 8080)))
    _hosts = environ.get('HOSTS')
    if _hosts:
        _hosts = tuple(_hosts.split(','))

    if not _hosts and isinstance(_hosts, tuple):
        print('Environment Variable HOSTS is invalid.')
        exit(1)

    REGISTRY.register(CustomCollector(_hosts))
    while True:
        time.sleep(1)
