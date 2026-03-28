from datasets import load_dataset

DATASET_ID = "MAlmasabi/Indirect-Prompt-Injection-BIPIA-GPT"
OUTPUT_BASENAME = "indirect_prompt_injection_bipia_gpt"

ds = load_dataset(
    DATASET_ID,
    cache_dir="data/hf_cache",
)

out_dir = f"data/{OUTPUT_BASENAME}"
ds.save_to_disk(out_dir)

# Export each split to single-file formats for EDA and interoperability.
# Note: CSV export uses pandas under the hood.
for split_name, split_dataset in ds.items():
    split_dataset.to_parquet(f"data/{OUTPUT_BASENAME}_{split_name}.parquet")
    split_dataset.to_csv(f"data/{OUTPUT_BASENAME}_{split_name}.csv")
