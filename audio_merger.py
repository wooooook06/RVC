import wave


def read_wav(file_path):
    with wave.open(file_path, 'rb') as wav:
        params = wav.getparams()
        frames = wav.readframes(params.nframes)
        audio_data = bytearray(frames)
    return audio_data, params


def merge_multiple_wavs(wav_paths):
    audio_data_list = []
    params_list = []
    for wav_path in wav_paths:
        audio_data, params = read_wav(wav_path)
        audio_data_list.append(audio_data)
        params_list.append(params)

    # Assume all WAV files have the same params (sampling rate, etc.)
    params = params_list[0]
    num_channels = params.nchannels
    sample_width = params.sampwidth

    # Combine audio data
    merged_data = bytearray()
    num_frames = min(params.nframes for params in params_list)
    for frame_idx in range(num_frames):
        frame_data = bytearray()
        for channel in range(num_channels):
            start_byte = frame_idx * num_channels * sample_width
            end_byte = start_byte + sample_width
            frame_data.extend(audio_data_list[channel][start_byte:end_byte])
        merged_data.extend(frame_data)

    return params, bytes(merged_data)


def write_wav(file_path, params, audio_data):
    with wave.open(file_path, 'wb') as wav:
        wav.setparams(params)
        wav.writeframes(audio_data)


wav_paths = ['vocal1.wav', 'vocal2.wav', 'vocal3.wav', 'vocal4.wav', 'vocal5.wav']

output_wav_path = 'vocal.wav'

params, merged_data = merge_multiple_wavs(wav_paths)

write_wav(output_wav_path, params, merged_data)
