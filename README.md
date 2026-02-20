The pipeline was tested in three ways:

First, a unit test failure was simulated by modifying train.py to save the model artifact under a different filename. This caused the test_artifact_created test to fail. The pipeline caught this and stopped at the Run Unit Tests step. The change was then reverted and the pipeline passed.

Second, the performance threshold was raised to 0.99 in check_performance.py and the model was intentionally weakened by setting max_iter=1 in train.py. This caused the pipeline to pass unit tests but fail at the Check Performance Threshold step. This showed that the quality gate works to block deployment of underperforming models. Both changes were then reverted.

Finally, the full pipeline was verified end-to-end with a successful run. A passing build triggers a deploy job that packages the model alongside a model card containing accuracy, commit SHA, and a timestamp. The packaged artifact is uploaded to GitHub Actions and versioned by commit SHA. This ensures each successful deployment is traceable to the exact code that produced it.
