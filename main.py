def original1():
    import wave

    CHANNELS = 1
    swidth = 2
    Change_RATE = 2

    sound = wave.open('sound.wav', 'rb')  # программа читает файл
    RATE = sound.getframerate()  # частота дискретизации(чтения)
    signal = sound.readframes(-1)  # Считывает и возвращает не более n кадров аудио в виде объекта bytes.

    done = wave.open('changed.wav', 'wb')  # программа пишет новый файл
    done.setnchannels(CHANNELS)  # установка количества каналов (в данном случае один)
    done.setsampwidth(swidth)  # установка ширины выборки в определенное количество байтов (здесь 2)
    done.setframerate(RATE * Change_RATE)  # установка частоты проигрывания фрэймов
    done.writeframes(signal)  # запись аудиодорожки без коррекции фрэймов
    done.close()  # программа закрыта

def slow():
    import wave

    CHANNELS = 1
    swidth = 2
    Change_RATE = 0.5

    sound = wave.open('sound.wav', 'rb')
    RATE = sound.getframerate()
    signal = sound.readframes(-1)

    done = wave.open('changedslow.wav', 'wb')
    done.setnchannels(CHANNELS)
    done.setsampwidth(swidth)
    done.setframerate(RATE * Change_RATE)
    done.writeframes(signal)
    done.close()
def speed():
    import wave
    CHANNELS = 1
    swidth = 2
    Change_RATE = 3.5

    sound = wave.open('sound.wav', 'rb')
    RATE = sound.getframerate()
    signal = sound.readframes(-1)

    done = wave.open('changedspeed.wav', 'wb')
    done.setnchannels(CHANNELS)
    done.setsampwidth(swidth)
    done.setframerate(RATE * Change_RATE)
    done.writeframes(signal)
    done.close()

original1()
slow()
speed()

