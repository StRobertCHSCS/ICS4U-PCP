using UnityEngine;
using System.Collections;

public class GlowOn : MonoBehaviour {
	public int lightOn = -1;
	public Material matWhite;
	public Material matBlack;
	public float targetTimeDuration = 2.0f;
	public float timeCounter = 0.0f;

	// Use this for initialization
	void Start () {

	}

	void Update() {
		
		if (lightOn == -1) {
			GetComponent<Renderer> ().material = matBlack;
		} else if (lightOn == 1) {
			GetComponent<Renderer> ().material = matWhite;
		}
		if (timeCounter > targetTimeDuration) {
			lightOn = -1;
			timeCounter = 0;

		}
		timeCounter += Time.deltaTime;
	}

	void OnCollisionEnter (Collision col){
		if (col.gameObject.tag == "Projectile") {
			lightOn *= -1;
			timeCounter = 0;
		} else if (col.gameObject.tag == "Player") {
			lightOn = 1;
			timeCounter = 0;

		}
	}
}
