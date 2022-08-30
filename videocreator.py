from moviepy.editor import TextClip
import moviepy.editor as mp
import moviepy.video.fx.all as vfx
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
import glob
import api
from moviepy.editor import *
from html import unescape


def getData():
    return api.getData()


def createVideoWithData():
    questionData = getData()
    questionDataSize = len(questionData)
    for i in range(0, questionDataSize):
        question = questionData[i].question
        question_html_parsed = unescape(question)
        correct_answer = questionData[i].correct_answer

        startVideoTemplate = mp.VideoFileClip(
            "assets/video-template.mp4")
        endVideoTemplate = mp.VideoFileClip(
            "assets/video-template.mp4")
        videoTemplate = mp.VideoFileClip(
            "assets/video-template.mp4")

        startVideoClip = startVideoTemplate.subclip(0, 1)
        endVideoClip = endVideoTemplate.subclip(6, 11)

        # clipping of the video
        # getting video for only starting 5 second
        questionClip = videoTemplate.subclip(1, 6)
        questionText = TextClip(question_html_parsed, fontsize=72,
                                font="Source-Code-Pro", color="black", align="center", method="caption", size=videoTemplate.size).set_position((0, -650)).set_duration(5)
        questionVideo = mp.CompositeVideoClip(
            [questionClip, questionText])

        questionAnswerText = TextClip(correct_answer, fontsize=121,
                                      font="Source-Code-Pro", color="white", align="center", size=videoTemplate.size).set_position(("center", 0)).set_duration(5)

        answerClip = mp.CompositeVideoClip([endVideoClip, questionAnswerText])
        resultVideo = mp.concatenate_videoclips(
            [startVideoClip, questionVideo, answerClip])

        resultVideo.write_videofile(f"output/{question}.mp4")


createVideoWithData()
