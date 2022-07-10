# ====================[ 사용할 라이브러리 선언 ]====================
import winsound
from pycaw.pycaw import AudioUtilities
# ============================================================


# ====================[ 상수(Constants) 영역 ]====================
MUTE_CODE = 1
UNMUTE_CODE = 0
target_process = "chrome.exe"
# ============================================================


class AutoPlayer:
    @staticmethod
    def muteTarget(target_process_name):
        sessions = AudioUtilities.GetAllSessions()
        for session in sessions:
            volume = session.SimpleAudioVolume
            if session.Process and session.Process.name() == target_process:
                volume.SetMute(MUTE_CODE, None)
        print("[!] 대상 프로세스(%s)를 음소거했습니다." % target_process_name)
        return

    @staticmethod
    def playSound():
        winsound.PlaySound("./resources/beep_5s.wav", winsound.SND_PURGE)
        return

    @staticmethod
    def unmuteTarget(target_process_name):
        sessions = AudioUtilities.GetAllSessions()
        for session in sessions:
            volume = session.SimpleAudioVolume
            if session.Process and session.Process.name() == target_process:
                volume.SetMute(UNMUTE_CODE, None)
        print("[!] 대상 프로세스(%s)를 음소거 해제했습니다." % target_process_name)
        return


def main():
    # 1. 대상 프로그램을 음소거함
    AutoPlayer.muteTarget(target_process)

    # 2. 소리 파일을 재생함
    AutoPlayer.playSound()

    # 3. 대상 프로그램을 음소거 해제함
    AutoPlayer.unmuteTarget(target_process)

    return


if __name__ == "__main__":
    main()
