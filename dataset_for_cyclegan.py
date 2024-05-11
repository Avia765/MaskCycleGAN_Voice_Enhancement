import os
import shutil
import soundfile as sf


def get_sound_duration_in_folder(folder_path):
    wav_files = [f for f in os.listdir(folder_path) if f.endswith('.wav')]
    time_duration = 0
    for wav_file in wav_files:
        filepath = os.path.join(folder_path, wav_file)
        f = sf.SoundFile(filepath)
        time_duration += f.frames / f.samplerate
    print('seconds = {}'.format(time_duration))
    return time_duration

def calc_all_folders_sound_duration():
    noisy_0db_clnsp0_to_2010 = '\\Users\\User\\PycharmProjects\\BarIlan2024\\GenerativeModels\\MaskCycleGAN-VC\\noisy_dataset\\noisy_training_0dB_clnsp0_to_2010'
    noisy_20db_clnsp0_to_2010 = '\\Users\\User\\PycharmProjects\\BarIlan2024\\GenerativeModels\\MaskCycleGAN-VC\\noisy_dataset\\noisy_training_20dB_clnsp0_to_2010'

    noisy_0db_clnsp2011_to_4020 = '\\Users\\User\\PycharmProjects\\BarIlan2024\\GenerativeModels\\MaskCycleGAN-VC\\noisy_dataset\\noisy_training_0dB_clnsp2011_to_4020'
    noisy_20db_clnsp2011_to_4020 = '\\Users\\User\\PycharmProjects\\BarIlan2024\\GenerativeModels\\MaskCycleGAN-VC\\noisy_dataset\\noisy_training_20dB_clnsp2011_to_4020'

    clean_clnsp2011_to_4020 = '\\Users\\User\\PycharmProjects\\BarIlan2024\\GenerativeModels\\MaskCycleGAN-VC\\noisy_dataset\\clean_training_clnsp2011_to_4020'
    clean_clnsp0_to_2010 = '\\Users\\User\\PycharmProjects\\BarIlan2024\\GenerativeModels\\MaskCycleGAN-VC\\noisy_dataset\\clean_training_clnsp0_to_2010'

    duration_in_hours_log = '\\Users\\User\\PycharmProjects\\BarIlan2024\\GenerativeModels\\MaskCycleGAN-VC\\noisy_dataset\\duration_log.txt'

    noisy_0db_cln0_to_2010_duration = get_sound_duration_in_folder(noisy_0db_clnsp0_to_2010)/60/60
    noisy_20db_cln0_to_2010_duration = get_sound_duration_in_folder(noisy_20db_clnsp0_to_2010)/60/60
    noisy_0db_cln2011_to_4020_duration = get_sound_duration_in_folder(noisy_0db_clnsp2011_to_4020)/60/60
    noisy_20db_cln2011_to_4020_duration = get_sound_duration_in_folder(noisy_20db_clnsp2011_to_4020)/60/60
    clean_clnsp2011_to_4020_duration = get_sound_duration_in_folder(clean_clnsp2011_to_4020)/60/60
    clean_clnsp0_to_2010_duration = get_sound_duration_in_folder(clean_clnsp0_to_2010)/60/60

    with open(duration_in_hours_log, 'w') as f:
        f.write('noisy_0db_cln0_to_2010_duration \t {} \n'.format(noisy_0db_cln0_to_2010_duration))
        f.write('noisy_20db_cln0_to_2010_duration \t {} \n'.format(noisy_20db_cln0_to_2010_duration))
        f.write('noisy_0db_cln2011_to_4020_duration \t {} \n'.format(noisy_0db_cln2011_to_4020_duration))
        f.write('noisy_20db_cln2011_to_4020_duration \t {} \n'.format(noisy_20db_cln2011_to_4020_duration))
        f.write('clean_clnsp2011_to_4020_duration \t {} \n'.format(clean_clnsp2011_to_4020_duration))
        f.write('clean_clnsp0_to_2010_duration \t {} \n'.format(clean_clnsp0_to_2010_duration))
    return


def main(train_or_eval_mode):
    # define speaker_a as noisy samples (half of the dataset, to ensure there will be on ovelapping)
    if train_or_eval_mode == 'train':
        resampled_noisy_path = os.path.join(os.getcwd(), 'resampled_NoisySpeech_training')
        resampled_clean_path = os.path.join(os.getcwd(), 'resampled_CleanSpeech_training')
        # define speaker_a as the noisy dataset
        noisy_0db_clnsp0_to_2010 = '\\Users\\User\\PycharmProjects\\BarIlan2024\\GenerativeModels\\MaskCycleGAN-VC\\noisy_dataset\\noisy_training\\noisy_training_0dB_clnsp0_to_2010'
        noisy_20db_clnsp0_to_2010 = '\\Users\\User\\PycharmProjects\\BarIlan2024\\GenerativeModels\\MaskCycleGAN-VC\\noisy_dataset\\noisy_training\\noisy_training_20dB_clnsp0_to_2010'

        noisy_0db_clnsp2011_to_4020 = '\\Users\\User\\PycharmProjects\\BarIlan2024\\GenerativeModels\\MaskCycleGAN-VC\\noisy_dataset\\noisy_training\\noisy_training_0dB_clnsp2011_to_4020'
        noisy_20db_clnsp2011_to_4020 = '\\Users\\User\\PycharmProjects\\BarIlan2024\\GenerativeModels\\MaskCycleGAN-VC\\noisy_dataset\\noisy_training\\noisy_training_20dB_clnsp2011_to_4020'

        clean_clnsp2011_to_4020 = '\\Users\\User\\PycharmProjects\\BarIlan2024\\GenerativeModels\\MaskCycleGAN-VC\\noisy_dataset\\noisy_training\\clean_training_clnsp2011_to_4020'
        clean_clnsp0_to_2010 = '\\Users\\User\\PycharmProjects\\BarIlan2024\\GenerativeModels\\MaskCycleGAN-VC\\noisy_dataset\\noisy_training\\clean_training_clnsp0_to_2010'

    elif train_or_eval_mode == 'eval':
        resampled_noisy_path = os.path.join(os.getcwd(), 'resampled_NoisySpeech_evaluation')
        resampled_clean_path = os.path.join(os.getcwd(), 'resampled_CleanSpeech_evaluation')
        # define speaker_a as the noisy dataset
        noisy_0db_clnsp0_to_530 = '\\Users\\User\\PycharmProjects\\BarIlan2024\\GenerativeModels\\MaskCycleGAN-VC\\noisy_dataset\\noisy_evaluation\\noisy_evaluation_0dB_clnsp0_to_530'
        noisy_20db_clnsp0_to_530 = '\\Users\\User\\PycharmProjects\\BarIlan2024\\GenerativeModels\\MaskCycleGAN-VC\\noisy_dataset\\noisy_evaluation\\noisy_evaluation_20dB_clnsp0_to_530'

        noisy_0db_clnsp531_to_1062 = '\\Users\\User\\PycharmProjects\\BarIlan2024\\GenerativeModels\\MaskCycleGAN-VC\\noisy_dataset\\noisy_evaluation\\noisy_evaluation_0dB_clnsp531_to_1062'
        noisy_20db_clnsp531_to_1062 = '\\Users\\User\\PycharmProjects\\BarIlan2024\\GenerativeModels\\MaskCycleGAN-VC\\noisy_dataset\\noisy_evaluation\\noisy_evaluation_20dB_clnsp531_to_1062'

        clean_clnsp531_to_1062 = '\\Users\\User\\PycharmProjects\\BarIlan2024\\GenerativeModels\\MaskCycleGAN-VC\\noisy_dataset\\noisy_evaluation\\clean_evaluation_clnsp531_to_1062'
        clean_clnsp0_to_530 = '\\Users\\User\\PycharmProjects\\BarIlan2024\\GenerativeModels\\MaskCycleGAN-VC\\noisy_dataset\\noisy_evaluation\\clean_evaluation_clnsp0_to_530'

    else:
        print('ERROR: need to choose train\eval mode')

    noisy_files = [f for f in os.listdir(resampled_noisy_path) if f.endswith('.wav')]
    clean_files = [f for f in os.listdir(resampled_clean_path) if f.endswith('.wav')]
    num_speakers = len(clean_files)

    for file in noisy_files:
        file1 = file.split('_')
        clnsp = file1[3].split('.')[0]
        # filter files based on their SNRs and clnsp IDs
        if (int(clnsp[5:]) <= num_speakers//2) and ((file1[2] == '0.0') or (file1[2] == '0')):
            if train_or_eval_mode == 'train':
                noisy_path = noisy_0db_clnsp0_to_2010
            elif train_or_eval_mode == 'eval':
                noisy_path = noisy_0db_clnsp0_to_530
            file1[2] = '0'
            newname = '_'.join(file1)
        elif (int(clnsp[5:]) <= num_speakers//2) and ((file1[2] == '20.0') or (file1[2] == '20')):
            if train_or_eval_mode == 'train':
                noisy_path = noisy_20db_clnsp0_to_2010
            elif train_or_eval_mode == 'eval':
                noisy_path = noisy_20db_clnsp0_to_530
            file1[2] = '20'
            newname = '_'.join(file1)
        elif (int(clnsp[5:]) > num_speakers//2) and ((file1[2] == '0.0') or (file1[2] == '0')):
            if train_or_eval_mode == 'train':
                noisy_path = noisy_0db_clnsp2011_to_4020
            elif train_or_eval_mode == 'eval':
                noisy_path = noisy_0db_clnsp531_to_1062
            file1[2] = '0'
            newname = '_'.join(file1)
        elif (int(clnsp[5:]) > num_speakers//2) and ((file1[2] == '20.0') or (file1[2] == '20')):
            if train_or_eval_mode == 'train':
                noisy_path = noisy_20db_clnsp2011_to_4020
            elif train_or_eval_mode == 'eval':
                noisy_path = noisy_20db_clnsp531_to_1062
            file1[2] = '20'
            newname = '_'.join(file1)
        else:
            print("ERROR - unexpected name of file")

        filepath = os.path.join(resampled_noisy_path, file)
        new_filepath = os.path.join(noisy_path, newname)
        #print(filepath, new_filepath)
        shutil.move(filepath, new_filepath)

    for file in clean_files:
        # filter files based on their clnsp IDs
        clnsp = file.split('.')[0]
        if (int(clnsp[5:]) <= (num_speakers//2)):
            if train_or_eval_mode == 'train':
                clean_path = clean_clnsp0_to_2010
            elif train_or_eval_mode == 'eval':
                clean_path = clean_clnsp0_to_530
        elif ((int(clnsp[5:]) > num_speakers//2)):
            if train_or_eval_mode == 'train':
                clean_path = clean_clnsp2011_to_4020
            elif train_or_eval_mode == 'eval':
                clean_path = clean_clnsp531_to_1062

        filepath = os.path.join(resampled_clean_path, file)
        new_filepath = os.path.join(clean_path, file)
        shutil.move(filepath, new_filepath)

    return


if __name__=="__main__":
    train_or_eval_mode = 'eval'   # 'train' or 'eval'
    main(train_or_eval_mode)
    #calc_all_folders_sound_duration()



