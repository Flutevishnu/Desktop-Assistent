import torch
from transformers import AutoModelForSpeechSeq2Seq, AutoProcessor, pipeline
from datasets import load_dataset


device = "cuda:0" if torch.cuda.is_available() else "cpu"
torch_dtype = torch.float16 if torch.cuda.is_available() else torch.float32

model_id = "distil-whisper/distil-large-v2"

model = AutoModelForSpeechSeq2Seq.from_pretrained(
    model_id, torch_dtype=torch_dtype, low_cpu_mem_usage=True, use_safetensors=True
)
model.to(device)

processor = AutoProcessor.from_pretrained(model_id)

pipe = pipeline(
    "automatic-speech-recognition",
    model=model,
    tokenizer=processor.tokenizer,
    feature_extractor=processor.feature_extractor,
    max_new_tokens=128,
    torch_dtype=torch_dtype,
    device=device,
)

dataset = load_dataset("hf-internal-testing/librispeech_asr_dummy", "clean", split="validation")
sample = dataset[1]["audio"]

# audio_file_path = r"C:/Users/vishn/Downloads/let_her_go.mp3"
# audio_file_path = r"C:/Users/vishn/Downloads/Da/Recording.m4a"
audio_file_path1 = r"C:/Users/vishn/Downloads/Da/output.wav"
# sampling_rate = 16000 


# result = pipe({"input_values": processor(audio_file_path, sampling_rate=sampling_rate)["input_values"]})
def speech_recognizer(audio_file_path):
    result = pipe(audio_file_path)
    print(result["text"])

speech_recognizer(
    audio_file_path1
)