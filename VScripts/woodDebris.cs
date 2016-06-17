using UnityEngine;
using System.Collections;

public class woodDebris : MonoBehaviour
{
    public static bool settled = false;
    private float settleLimit = 0.65f;
    private float settleCounter = 0;
	private bool inMotion = false;
    // Use this for initialization
    void Start()
    {

    }

    // Update is called once per frame
    void Update()
    {
		settleCounter += Time.deltaTime;
		foreach (Transform child in transform) {
			if (child.GetComponent<Rigidbody> ().velocity.magnitude > 0) {
				inMotion = true;
			}
		}

		while ((settleCounter > settleLimit) && inMotion == false)
        {
            settled = true;
            settleCounter = 0;
        }

		if (settled) {
			
			foreach (Transform child in this.transform) {
				Destroy (child.GetComponent<Rigidbody>());
			}

		}
		inMotion = false;
    }
}
